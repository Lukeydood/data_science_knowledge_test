# Data Scientist Knowledge Test – Practice Papers

Free, self-marking practice papers for the **Data Scientist integrated degree apprenticeship (ST0585)** End-Point Assessment **Knowledge Test** (30 multiple-choice questions on KSBs 3.1–5.3).

- **730 questions**: 652 on the assessed KSBs (40+ distinct concepts per KSB) plus 78 optional general data science questions
- Every paper covers every KSB, with options shuffled and no repeated concepts
- Answers are written so the correct option can't be spotted by length or wording (checked automatically)
- Marks itself: score out of 30, **PASS/FAIL against a 60% pass mark (18/30)**, wrong answers highlighted in red with the correct answer and an explanation, and a per-KSB breakdown
- Untimed by default
- Use it as a **web app** (GitHub Pages), or generate HTML papers with Python and save them wherever you choose – no installs beyond Python 3.9+

---

## Option 1 – Use the web app

Open the site (hosted free on GitHub Pages), choose your settings and press **Start new paper**:

- **Questions** – defaults to 30, like the real test
- **Pass mark** – defaults to 60%
- **Timer** – blank for untimed (default), or enter minutes for a countdown
- **Assessed KSBs** – untick any to focus on weak areas
- **Include general data science questions** – off by default; tick to mix in Python, SQL, experiments, visualisation and ethics questions that go beyond the KSBs
- **Don't say how many options to select** – a harder mode

**Download paper** saves a paper as a standalone HTML file to sit offline. In Chrome and Edge a *Save as* window lets you choose the folder and file name; other browsers save it the way they normally handle downloads. You can also download the paper you're sitting from the bar at the top.

The app remembers which questions you've seen (in your own browser only) and avoids repeating them until you've worked through each topic.

Everything runs in the browser: no accounts, no server, and no answers are sent anywhere.

## Option 2 – Generate papers with Python

1. Install Python 3.9 or later (check with `python --version`).
2. In a terminal in this folder, run:

   ```bash
   python generate_exams.py
   ```

   (On macOS/Linux you may need `python3`.)
3. A folder picker opens: choose where to save the paper. (Without a desktop, you're asked to type a folder instead.)
4. Open the saved file, e.g. `DS_KnowledgeTest_Practice_20261017-1930_seed123456_01.html`, in any browser. It works offline and on a phone.

### Common commands

| What you want | Command |
|---|---|
| One 30-question paper (asks where to save) | `python generate_exams.py` |
| Five papers with no repeated questions | `python generate_exams.py -n 5` |
| **Include general data science questions** | `python generate_exams.py --include-general` |
| General questions only | `python generate_exams.py --ksb GEN` |
| Practise weak KSBs only | `python generate_exams.py --ksb 4.1 4.2` |
| Change the pass mark | `python generate_exams.py --pass-percent 70` (or `--pass-mark 21`) |
| Add a countdown timer | `python generate_exams.py --time-limit 60` |
| Harder: don't say how many to tick | `python generate_exams.py --hide-answer-count` |
| Short revision quiz | `python generate_exams.py -q 10` |
| Regenerate the exact same paper | `python generate_exams.py --seed 123456` |
| Save to a folder without being asked | `python generate_exams.py -o ~/Desktop/papers` |
| Question counts per KSB | `python generate_exams.py --stats` |
| Export the bank to JSON | `python generate_exams.py --export-bank bank.json` |

Run `python generate_exams.py --help` for everything.


---

## Project layout

```
generate_exams.py        CLI: samples questions and writes self-marking HTML papers
build_site.py            Builds the web app into site/index.html
exam_template.html       Self-marking paper (HTML/CSS/JS, no external dependencies)
web/app_template.html    Web app settings page; embeds the bank and paper template
question_bank/
  ksb_*.py               Assessed KSB questions (3.1–5.3), two modules per KSB
  gen_*.py               Optional general data science questions
  cues.py                Checks that answers can't be guessed from length/wording
.github/workflows/pages.yml   Validate on every push/PR; deploy to Pages from main
```

## Adding questions

Add to the relevant `question_bank/ksb_*.py` or `gen_*.py` file. New `ksb_*.py` / `gen_*.py` modules are picked up automatically.

```python
q("concept-tag", "Which TWO ...?",
  ["option A", "option B", "option C", "option D"],
  "AC", "Why A and C are correct.")
```

- Reuse a concept tag for a variant of an existing idea (variants never appear on the same paper).
- Write "TWO" or "THREE" in capitals in multi-answer questions.
- Keep options parallel and similar in length, and avoid absolute words ("always", "never") in wrong options.

Then check the bank and preview the site:

```bash
python -m question_bank.cues     # validates the bank and lists any answer giveaways
python build_site.py             # builds site/index.html to open in a browser
```

The same checks run automatically on every push; a failing check stops deployment.

## Licence and disclaimer

Code and questions: MIT licence (see [LICENSE](LICENSE)). KSB wording from the ST0585 standard is © Crown copyright, reused under the Open Government Licence v3.0.

These are **unofficial** practice questions written from the published KSBs. They are not the EPAO's questions and real papers will be worded differently.
