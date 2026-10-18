"""Question bank for the Data Scientist (ST0585) EPA knowledge test.

Every module in this package named `ksb_*.py` (assessed KSBs 3.1–5.3) or
`gen_*.py` (optional general data science revision) defines a QUESTIONS list.
New modules are picked up automatically.

`load_bank()` returns every question as a dict with keys:
    id, ksb, ksb_title, concept, question, options (4), answer (list of indexes), explanation,
    search (a broad-theme Google search phrase, shown after marking)
"""

import importlib
import pkgutil

from .themes import CONCEPT_THEME

GENERAL = "GEN"
_COUNT_WORDS = {2: "TWO", 3: "THREE"}


def _ksb_sort_key(k):
    return (1, ()) if k == GENERAL else (0, tuple(int(p) for p in k.split(".")))


def _modules():
    names = sorted(m.name for m in pkgutil.iter_modules(__path__)
                   if m.name.startswith(("ksb_", "gen_")))
    return [importlib.import_module(f"{__name__}.{n}") for n in names]


def load_bank():
    bank = [dict(q, search=CONCEPT_THEME.get(q["concept"], "")) for m in _modules() for q in m.QUESTIONS]
    bank.sort(key=lambda q: (_ksb_sort_key(q["ksb"]), q["id"]))
    validate(bank)
    return bank


def _areas():
    areas = {}
    for m in _modules():
        for q in m.QUESTIONS:
            areas.setdefault(q["ksb"], q["ksb_title"])
    return {k: areas[k] for k in sorted(areas, key=_ksb_sort_key)}


KSBS = _areas()                                         # every area, incl. GEN
ASSESSED_KSBS = {k: v for k, v in KSBS.items() if k != GENERAL}


def validate(bank):
    """Raise ValueError if any question is malformed. Returns the bank."""
    errors = []
    ids = set()
    for q in bank:
        qid = q.get("id", "?")
        if qid in ids:
            errors.append(f"{qid}: duplicate id")
        ids.add(qid)
        if len(q["options"]) != 4:
            errors.append(f"{qid}: must have exactly 4 options")
        if len(set(o.lower() for o in q["options"])) != len(q["options"]):
            errors.append(f"{qid}: duplicate options")
        if not q["answer"] or any(i not in range(4) for i in q["answer"]):
            errors.append(f"{qid}: answer indexes invalid")
        if len(q["answer"]) == 4:
            errors.append(f"{qid}: all four options correct is not a useful question")
        n = len(q["answer"])
        word = _COUNT_WORDS.get(n)
        if n > 1 and word not in q["question"]:
            errors.append(f"{qid}: multi-answer question should say 'Which {word}...'")
        if n == 1 and any(w in q["question"] for w in _COUNT_WORDS.values()):
            errors.append(f"{qid}: says TWO/THREE but has a single answer")
        if not q["explanation"]:
            errors.append(f"{qid}: missing explanation")
        if not q.get("search"):
            errors.append(f"{qid}: concept {q['concept']!r} has no search theme in question_bank/themes.py")
        for opt in q["options"]:
            low = opt.lower()
            if "all of the above" in low or "none of the above" in low or "both a and b" in low:
                errors.append(f"{qid}: avoid 'all/none of the above' (options are shuffled)")
    unused = set(CONCEPT_THEME) - {q["concept"] for q in bank}
    if unused and len({q["ksb"] for q in bank}) == len({k.split(":")[0] for k in CONCEPT_THEME}):
        errors.append(f"themes.py lists concepts not in the bank: {sorted(unused)}")
    if errors:
        raise ValueError("Question bank errors:\n  " + "\n  ".join(errors))
    return bank
