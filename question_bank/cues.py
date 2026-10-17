"""Checks that the correct option can't be spotted without knowing the subject.

Test-wise candidates pick the longest / most qualified option, avoid options
with absolute words ("always", "never"), and dismiss obviously silly options.
These checks catch the first two automatically; the third is a writing rule
(see methodology.md).

Run:  python -m question_bank.cues
"""

import re

# Correct option may be at most this much longer than the longest distractor.
MAX_LENGTH_RATIO = 1.25
# Across the bank, the correct option should be the longest in no more than this share
# of single-answer questions (25% would be chance with four options).
MAX_LONGEST_SHARE = 0.40

ABSOLUTE = re.compile(r"\b(always|never|guarantee[sd]?|impossible|cannot|only ever|entirely|every time)\b", re.I)


def question_issues(q):
    issues = []
    opts, ans = q["options"], q["answer"]
    lens = [len(o) for o in opts]
    correct = [lens[i] for i in ans]
    wrong = [lens[i] for i in range(4) if i not in ans]
    if (max(correct) > MAX_LENGTH_RATIO * max(wrong) and min(correct) > max(wrong)
            and max(correct) - max(wrong) > 8):  # ignore tiny differences between short options
        issues.append(f"correct option(s) clearly longest ({max(correct)} vs {max(wrong)} chars)")
    if max(correct) < 0.5 * min(wrong) and min(wrong) - max(correct) > 8:
        issues.append(f"correct option clearly shortest ({max(correct)} vs {min(wrong)} chars)")
    correct_abs = any(ABSOLUTE.search(opts[i]) for i in ans)
    for i in range(4):
        if i not in ans and ABSOLUTE.search(opts[i]) and not correct_abs:
            issues.append(f"absolute wording only in a distractor: {opts[i]!r}")
    return issues


def bank_report(bank):
    per_q = {q["id"]: question_issues(q) for q in bank}
    per_q = {k: v for k, v in per_q.items() if v}
    single = [q for q in bank if len(q["answer"]) == 1]
    # Count questions where the correct option is the single, strictly longest option.
    longest = sum(1 for q in single
                  if len(q["options"][q["answer"][0]]) > max(len(o) for i, o in enumerate(q["options"])
                                                              if i != q["answer"][0]))
    return per_q, longest / len(single)


if __name__ == "__main__":
    from question_bank import load_bank
    issues, share = bank_report(load_bank())
    for qid, msgs in issues.items():
        for m in msgs:
            print(f"{qid}: {m}")
    print(f"\n{len(issues)} questions with cues; correct option is longest in {share:.0%} "
          f"of single-answer questions (target ≤ {MAX_LONGEST_SHARE:.0%}, chance = 25%)")
    if issues or share > MAX_LONGEST_SHARE:
        raise SystemExit(1)
