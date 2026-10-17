#!/usr/bin/env python3
"""Generate self-marking HTML practice papers for the Data Scientist (ST0585)
EPA knowledge test, covering KSBs 3.1–5.3, with an optional general
data science pool.

Examples
--------
    python generate_exams.py                      # one paper; asks where to save it
    python generate_exams.py -o papers            # save into a folder without asking
    python generate_exams.py -n 5                 # five papers with minimal overlap
    python generate_exams.py --ksb 4.1 4.2        # practise specific KSBs only
    python generate_exams.py --include-general    # mix in general data science questions
    python generate_exams.py --ksb GEN            # general questions only
    python generate_exams.py --time-limit 60      # optional countdown (untimed by default)
    python generate_exams.py --seed 42            # reproducible paper(s)
    python generate_exams.py --stats              # show question bank coverage
    python generate_exams.py --export-bank bank.json

Only the Python standard library is required.
"""

from __future__ import annotations

import argparse
import base64
import json
import math
import random
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from question_bank import ASSESSED_KSBS, GENERAL, KSBS, load_bank

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE / "exam_template.html"


def choose_out_dir() -> Path:
    """Ask the user where to save: a folder picker if a desktop is available, else a typed path."""
    start = Path.home() / "Downloads"
    if not start.exists():
        start = Path.cwd()
    try:
        import tkinter as tk
        from tkinter import filedialog

        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        chosen = filedialog.askdirectory(title="Choose where to save the practice paper(s)",
                                         initialdir=str(start), mustexist=False)
        root.destroy()
        if chosen:
            return Path(chosen)
        sys.exit("No folder chosen, so nothing was saved.")
    except SystemExit:
        raise
    except Exception:
        pass  # no display (e.g. a server) – fall back to typing a path
    if not sys.stdin.isatty():
        sys.exit("No output folder given. Use -o/--out-dir to say where to save the paper(s).")
    typed = input(f"Folder to save the paper(s) in [{start}]: ").strip().strip('"')
    return Path(typed) if typed else start


# --------------------------------------------------------------------------- #
# Selection
# --------------------------------------------------------------------------- #
def allocate(n_questions: int, ksbs: list[str], rng: random.Random,
             caps: dict[str, int] | None = None) -> dict[str, int]:
    """Split n_questions as evenly as possible across KSBs (round-robin in a
    random order), never giving a KSB more questions than it has distinct
    concepts (`caps`). When the split isn't exact, which KSBs get the extra
    question is random, so a set of papers is balanced on average."""
    caps = caps or {}
    order = ksbs[:]
    rng.shuffle(order)
    quota = {k: 0 for k in ksbs}
    remaining = n_questions
    while remaining:
        progressed = False
        for k in order:
            if remaining and quota[k] < caps.get(k, n_questions):
                quota[k] += 1
                remaining -= 1
                progressed = True
        if not progressed:
            raise ValueError("Not enough distinct concepts in the selected KSBs for this many questions")
    return quota


class Sampler:
    """Draws questions per KSB from shuffled 'decks' so that, across a set of
    papers, no question repeats until that KSB's deck has been used up, and no
    paper ever contains two variants of the same concept."""

    def __init__(self, bank: list[dict], rng: random.Random):
        self.rng = rng
        self.by_ksb: dict[str, list[dict]] = defaultdict(list)
        for q in bank:
            self.by_ksb[q["ksb"]].append(q)
        self.decks: dict[str, list[dict]] = {k: [] for k in self.by_ksb}

    def _refill(self, ksb: str):
        deck = self.by_ksb[ksb][:]
        self.rng.shuffle(deck)
        self.decks[ksb].extend(deck)

    def draw(self, ksb: str, n: int, used_concepts: set[str]) -> list[dict]:
        picked: list[dict] = []
        refills = 0
        while len(picked) < n:
            if not self.decks[ksb]:
                if refills >= 2:
                    raise ValueError(f"KSB {ksb} does not have {n} distinct concepts for one paper")
                self._refill(ksb)
                refills += 1
            # Take the first question in the deck whose concept isn't already on the paper.
            for i, q in enumerate(self.decks[ksb]):
                if q["concept"] not in used_concepts:
                    picked.append(self.decks[ksb].pop(i))
                    used_concepts.add(q["concept"])
                    break
            else:
                # Everything left in the deck clashes; top the deck up and try again.
                if refills >= 2:
                    raise ValueError(f"KSB {ksb} does not have {n} distinct concepts for one paper")
                self._refill(ksb)
                refills += 1
        return picked


def pass_mark_for(n_questions: int, percent: float) -> int:
    """Smallest whole score that is at least `percent`% of the paper (60% of 30 → 18)."""
    return max(1, math.ceil(round(n_questions * percent / 100, 9)))


def shuffle_options(q: dict, rng: random.Random) -> dict:
    order = list(range(4))
    rng.shuffle(order)
    return {
        **q,
        "options": [q["options"][i] for i in order],
        "answer": sorted(order.index(a) for a in q["answer"]),
    }


def build_paper(sampler: Sampler, ksbs: list[str], n_questions: int, rng: random.Random,
                paper_index: int, shuffle_opts: bool) -> list[dict]:
    caps = {k: len({q["concept"] for q in sampler.by_ksb[k]}) for k in ksbs}
    quota = allocate(n_questions, ksbs, rng, caps)
    used: set[str] = set()
    questions: list[dict] = []
    for ksb in ksbs:
        questions.extend(sampler.draw(ksb, quota[ksb], used))
    rng.shuffle(questions)  # interleave KSBs, as in the real test
    if shuffle_opts:
        questions = [shuffle_options(q, rng) for q in questions]
    return questions


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #
def render_html(questions: list[dict], *, paper_id: str, title: str, time_limit: int,
                pass_mark: int | None, hide_answer_count: bool, bank_size: int) -> str:
    key = {
        "answers": [q["answer"] for q in questions],
        "explanations": [q["explanation"] for q in questions],
    }
    data = {
        "paper_id": paper_id,
        "generated": datetime.now().strftime("%d %b %Y %H:%M"),
        "bank_size": bank_size,
        "time_limit_min": time_limit,
        "pass_mark": pass_mark,
        "hide_answer_count": hide_answer_count,
        "questions": [
            {
                "id": q["id"],
                "ksb": q["ksb"],
                "ksb_title": q["ksb_title"],
                "question": q["question"],
                "options": q["options"],
                "select": len(q["answer"]),
            }
            for q in questions
        ],
        "key": base64.b64encode(json.dumps(key).encode("utf-8")).decode("ascii"),
    }
    # Escape "</" so question text can never close the <script> tag early.
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.read_text(encoding="utf-8")
    html = html.replace("/*__EXAM_DATA__*/null", payload)
    html = html.replace("__SHORT_TITLE__", _escape(f"Practice paper {paper_id}"))
    html = html.replace("__TITLE__", _escape(title))
    return html


def _escape(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def parse_args(argv=None):
    p = argparse.ArgumentParser(description="Generate self-marking HTML practice papers (KSBs 3.1–5.3).")
    p.add_argument("-n", "--num-papers", type=int, default=1, help="number of papers to generate (default 1)")
    p.add_argument("-q", "--questions", type=int, default=30, help="questions per paper (default 30)")
    p.add_argument("-o", "--out-dir", type=Path, default=None,
                   help="folder to save papers in (if omitted, you are asked to choose one)")
    p.add_argument("--seed", type=int, default=None, help="random seed for reproducible papers")
    p.add_argument("--ksb", nargs="+", metavar="KSB",
                   help="restrict to these KSBs, e.g. --ksb 3.2 4.1 (use GEN for general questions only)")
    p.add_argument("--include-general", action="store_true",
                   help="also draw from the general data science pool (not assessed KSBs); off by default")
    p.add_argument("--time-limit", type=int, default=0,
                   help="optional countdown in minutes (default 0 = untimed)")
    p.add_argument("--pass-percent", type=float, default=60,
                   help="pass mark as a percentage of questions, rounded up (default 60 → 18/30)")
    p.add_argument("--pass-mark", type=int, default=None,
                   help="pass mark as an absolute score; overrides --pass-percent")
    p.add_argument("--hide-answer-count", action="store_true",
                   help="don't say how many options to select; every question uses checkboxes")
    p.add_argument("--no-shuffle-options", action="store_true", help="keep options in bank order")
    p.add_argument("--prefix", default="DS_KnowledgeTest_Practice", help="output filename prefix")
    p.add_argument("--stats", action="store_true", help="print question bank coverage and exit")
    p.add_argument("--export-bank", type=Path, metavar="FILE", help="write the whole bank to JSON and exit")
    return p.parse_args(argv)


def print_stats(bank):
    by = defaultdict(list)
    for q in bank:
        by[q["ksb"]].append(q)
    print(f"{'KSB':<5} {'Qs':>4} {'Concepts':>9} {'Multi':>6}  Area")
    for k in KSBS:
        qs = by[k]
        print(f"{k:<5} {len(qs):>4} {len({q['concept'] for q in qs}):>9} "
              f"{sum(len(q['answer']) > 1 for q in qs):>6}  {KSBS[k]}")
    print(f"Total {len(bank)} questions, {len({q['concept'] for q in bank})} distinct concepts")


def main(argv=None) -> list[Path]:
    args = parse_args(argv)
    bank = load_bank()

    if args.stats:
        print_stats(bank)
        return []
    if args.export_bank:
        args.export_bank.write_text(json.dumps(bank, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Exported {len(bank)} questions to {args.export_bank}")
        return []

    ksbs = list(ASSESSED_KSBS) + ([GENERAL] if args.include_general else [])
    if args.ksb:
        unknown = [k for k in args.ksb if k not in KSBS]
        if unknown:
            sys.exit(f"Unknown KSB(s): {', '.join(unknown)}. Choose from: {', '.join(KSBS)}")
        ksbs = [k for k in KSBS if k in args.ksb or (k == GENERAL and args.include_general)]
    bank = [q for q in bank if q["ksb"] in ksbs]
    if args.questions < 1 or args.num_papers < 1:
        sys.exit("--questions and --num-papers must be at least 1")
    if args.pass_mark is not None and not 0 < args.pass_mark <= args.questions:
        sys.exit("--pass-mark must be between 1 and the number of questions")
    if not 0 < args.pass_percent <= 100:
        sys.exit("--pass-percent must be between 0 and 100")
    max_q = len({q["concept"] for q in bank})
    if args.questions > max_q:
        print(f"Note: the selected KSB(s) have {max_q} distinct concepts, so each paper will have {max_q} questions.")
        args.questions = max_q
    if args.pass_mark is None:
        args.pass_mark = pass_mark_for(args.questions, args.pass_percent)
    args.pass_mark = min(args.pass_mark, args.questions)
    if args.questions < len(ksbs):
        print(f"Note: {args.questions} questions across {len(ksbs)} KSBs – some KSBs won't appear on each paper.")

    seed = args.seed if args.seed is not None else random.randrange(10**6)
    rng = random.Random(seed)
    sampler = Sampler(bank, rng)

    if args.out_dir is None:
        args.out_dir = choose_out_dir()
    args.out_dir = args.out_dir.expanduser()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M")
    written = []
    for i in range(args.num_papers):
        paper_ksbs = ksbs
        if args.questions < len(ksbs):
            start = (i * args.questions) % len(ksbs)
            paper_ksbs = (ksbs[start:] + ksbs[:start])[: args.questions]
        questions = build_paper(sampler, paper_ksbs, args.questions, rng, i, not args.no_shuffle_options)
        paper_id = f"{seed}-{i + 1:02d}"
        html = render_html(
            questions,
            paper_id=paper_id,
            title=f"Data Scientist Knowledge Test – Practice Paper {i + 1}"
                  + (" (incl. general questions)" if GENERAL in ksbs and len(ksbs) > 1 else ""),
            time_limit=args.time_limit,
            pass_mark=args.pass_mark,
            hide_answer_count=args.hide_answer_count,
            bank_size=len(bank),
        )
        path = args.out_dir / f"{args.prefix}_{stamp}_seed{seed}_{i + 1:02d}.html"
        path.write_text(html, encoding="utf-8")
        written.append(path)
        print(f"Wrote {path}")
    print(f"Done. Seed {seed} – rerun with --seed {seed} to regenerate the same paper(s).")
    return written


if __name__ == "__main__":
    main()
