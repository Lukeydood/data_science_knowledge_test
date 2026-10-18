"""General revision: UK public-sector analysis guidance and governance (not assessed KSBs).

These were moved out of the assessed KSB pools because they only apply to
people working in UK government and the wider public sector.
"""
from ._helpers import make_builder

q, QUESTIONS = make_builder("GEN", "General data science (optional revision beyond the assessed KSBs)", start=201)

q("aqua-book", "Which UK government publication provides guidance on producing quality analysis and the quality assurance of analytical models?",
  ["The Aqua Book", "The Green Book", "The Magenta Book", "The Orange Book"],
  "A", "Aqua Book = analytical quality assurance; Green Book = appraisal (incl. cost-benefit); Magenta Book = evaluation; Orange Book = risk management.")
q("green-book", "Which HM Treasury guidance sets out how to appraise policies, programmes and projects, including cost-benefit analysis?",
  ["The Green Book", "The Aqua Book", "The Magenta Book", "The Orange Book"],
  "A", "The Green Book is central government guidance on appraisal.")
q("magenta-book", "Which HM Treasury guidance focuses on how to design and carry out evaluation of policies?",
  ["The Magenta Book", "The Aqua Book", "The Green Book", "The Orange Book"],
  "A", "The Magenta Book covers evaluation design and methods.")
q("qa-roles", "In analytical quality assurance (e.g. the Aqua Book), which TWO roles are typically defined?",
  ["A commissioner who sets the question and uses the results", "An assurer who checks the analysis is fit for purpose", "A marketer who publicises the findings externally", "A procurer who buys the software used for the model"],
  "AB", "The Aqua Book defines commissioner, analyst, assurer and approver roles.")
q("statistics-code", "The Code of Practice for Statistics is built around which three pillars?",
  ["Trustworthiness, Quality and Value", "Accuracy, Timeliness and Coverage", "Transparency, Fairness and Accountability", "Validity, Reliability and Relevance"],
  "A", "The UK Statistics Authority's Code rests on Trustworthiness, Quality and Value.")
q("algorithmic-transparency", "The UK Algorithmic Transparency Recording Standard asks public bodies to:",
  ["Publish information about algorithmic tools used in decisions", "Release the source code of every model they use as open source", "Obtain consent before any algorithm processes personal data", "Stop using machine learning for decisions about individuals"],
  "A", "It provides a standard format for publishing what tools are used, how and why.")
q("equality-duty", "Which UK legal duty requires public bodies to consider the impact of their decisions, including automated ones, on people with protected characteristics?",
  ["The Public Sector Equality Duty", "The Freedom of Information Act", "The Official Secrets Act", "The Statistics and Registration Act"],
  "A", "The PSED (Equality Act 2010, s149) applies to decisions supported by data and algorithms.")
q("rap", "Reproducible Analytical Pipelines (RAP), promoted across UK government, aim to:",
  ["Replace manual spreadsheet processes with tested, version-controlled code", "Standardise all government analysis on a single commercial analytics platform", "Publish all analytical outputs as open data within one month", "Require every model to be independently audited before use"],
  "A", "RAP improves the quality, speed and auditability of analysis through automation and good software practice.")
q("information-asset-owner", "In UK public sector information governance, who is accountable for a particular dataset and its risks?",
  ["The Information Asset Owner", "The newest analyst to use it", "The cloud provider hosting it", "The person who last edited it"],
  "A", "IAOs are senior staff accountable for information assets; data stewards often handle day-to-day management.")
