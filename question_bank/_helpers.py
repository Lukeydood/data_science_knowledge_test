"""Small helper used by every KSB module to declare questions compactly.

Each question is a plain dict so the bank can be exported to JSON and
edited by people who do not want to touch Python.
"""

LETTERS = "ABCD"


def make_builder(ksb: str, ksb_title: str, start: int = 1):
    """Return a function `q(...)` bound to one KSB, plus the list it fills.

    `start` sets the first id number, so a second module for the same KSB
    (e.g. start=101) cannot clash with the first.
    """
    questions = []

    def q(concept: str, text: str, options: list, answer: str, explanation: str):
        idx = len(questions) + start
        questions.append(
            {
                "id": f"{ksb}-{idx:03d}",
                "ksb": ksb,
                "ksb_title": ksb_title,
                "concept": f"{ksb}:{concept}",
                "question": text.strip(),
                "options": [o.strip() for o in options],
                "answer": sorted(LETTERS.index(a) for a in answer.upper()),
                "explanation": explanation.strip(),
            }
        )

    return q, questions
