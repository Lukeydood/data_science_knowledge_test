from ._helpers import make_builder

q, QUESTIONS = make_builder("3.3", "Data-driven decision making and the good use of evidence and analytics", start=101)

q("ecological-fallacy", "Areas with higher average income have lower recycling rates, so a manager concludes that richer individuals recycle less. What error is this?",
  ["Ecological fallacy", "Survivorship bias", "Base rate neglect", "Recall bias in surveys"],
  "A", "Group-level associations do not necessarily hold for individuals within the groups.")
q("reverse-causation", "Restaurants with more hygiene inspections have more recorded violations. Which explanation should be considered before concluding inspections cause incidents?",
  ["Reverse causation: problem restaurants get inspected more", "Regression to the mean across all of the restaurants", "Survivorship bias among restaurants still trading", "Simpson's paradox caused by grouping restaurants by region"],
  "A", "The direction of causation may run the other way; inspections may also simply detect more violations.")
q("hawthorne", "Staff productivity rises during a trial simply because staff know they are being observed. This is the:",
  ["Hawthorne effect", "Placebo effect", "Halo effect", "Dunning–Kruger effect"],
  "A", "Being studied changes behaviour; control groups who are also observed help separate this from the intervention.")
q("sunk-cost", "A team continues funding a failing project mainly because a lot has already been spent on it. This is:",
  ["The sunk cost fallacy", "Loss-aversion hedging", "The planning fallacy", "Status quo analysis"],
  "A", "Decisions should consider future costs and benefits; money already spent cannot be recovered.")
q("optimism-bias", "Project planners routinely underestimate costs and timescales, so appraisal guidance adds an uplift to correct for:",
  ["Optimism bias", "Survivorship bias", "Selection bias", "Confirmation bias"],
  "A", "Appraisal guidance (e.g. HM Treasury's Green Book) adds optimism bias uplifts because planners systematically underestimate costs and durations.")
q("groupthink", "A project board agrees unanimously without anyone challenging the evidence, to preserve harmony. This is:",
  ["Groupthink", "Anchoring", "Framing", "Herding"],
  "A", "Groupthink suppresses dissent; structured challenge, red-teaming and independent review counter it.")
q("framing", "Describing a treatment as having a '90% survival rate' rather than a '10% mortality rate' changes how people choose. This is the:",
  ["Framing effect", "Anchoring effect", "Decoy effect", "Bandwagon effect"],
  "A", "Logically equivalent descriptions can lead to different decisions depending on presentation.")
q("evidence-strength", "Which TWO features make a piece of analytical evidence more trustworthy for a decision?",
  ["Transparent methods and data that others can check", "Results that have been replicated or triangulated", "A large dashboard with many charts and metrics", "Strong endorsement from the most senior stakeholder"],
  "AB", "Reproducibility, transparency and corroboration matter more than presentation or seniority.")
q("triangulation", "Using several independent sources or methods to check whether they point to the same conclusion is called:",
  ["Triangulation", "Interpolation", "Stratification", "Calibration"],
  "A", "Agreement across independent evidence increases confidence; disagreement flags where to dig.")
q("leading-lagging", "Which is an example of a leading indicator of customers cancelling a subscription?",
  ["A fall in a customer's logins in recent weeks", "Number of customers who cancelled last month", "Revenue lost from customers who left", "Cost of win-back offers sent to past customers"],
  "A", "Leading indicators move before the outcome; the others are lagging indicators that measure what already happened.")
q("smart", "A good KPI should be SMART. What does the 'M' stand for?",
  ["Measurable", "Meaningful", "Monitored", "Modelled"],
  "A", "Specific, Measurable, Achievable (or Agreed), Relevant, Time-bound.")
q("vanity-metrics", "Why can 'number of dashboard views' be a poor measure of an analytics team's impact?",
  ["It measures activity, not whether decisions or outcomes improved", "It is hard to collect reliably from most dashboard platforms", "It is too strongly correlated with the size of the organisation", "It changes too slowly to be useful for monthly reporting"],
  "A", "Vanity metrics are easy to count but weakly linked to value; focus on decisions informed and outcomes changed.")
q("decision-tree-analysis", "A decision tree for choosing between options, with chance nodes and outcome values, is used to:",
  ["Compare the expected value of choices under uncertainty", "Classify records into groups using learned split rules", "Show the reporting hierarchy of the whole project team", "Record the order in which data pipeline tasks run"],
  "A", "Decision analysis trees combine probabilities and payoffs; ML decision trees (second option) are a different tool.")
q("sensitivity-analysis", "Re-running a cost-benefit model with key assumptions varied to see whether the recommendation changes is:",
  ["Sensitivity analysis", "Regression analysis", "Variance analysis", "Cohort analysis"],
  "A", "Sensitivity analysis shows how robust a conclusion is to uncertain inputs; switching values reveal the critical assumptions.")
q("scenario-analysis", "Why might decision-makers be shown 'low', 'central' and 'high' scenarios rather than one forecast?",
  ["To show the range of plausible outcomes under different assumptions", "To let them choose the scenario that best supports their preference", "To avoid stating which assumptions drive the central forecast", "To satisfy a requirement that every chart shows three lines"],
  "A", "Scenarios communicate uncertainty and support robust decisions that work across futures.")
q("proportionate-qa", "According to good analytical QA practice, how much assurance should an analysis receive?",
  ["Proportionate to its risk, complexity and impact on decisions", "The same full independent external review for every piece of work", "Only enough to satisfy the person who commissioned it", "None if the analyst is experienced in the method used"],
  "A", "Assurance effort should scale with the stakes and complexity of the analysis.")
q("model-risk", "Which TWO are signs that a model used for a decision carries high model risk?",
  ["It is complex, poorly documented and rarely validated", "Its outputs directly drive a high-impact decision", "It is simple, well tested and peer reviewed", "Its outputs are used only for exploratory charts"],
  "AB", "Model risk grows with complexity, poor documentation and the impact of decisions depending on it.")
q("bias-in-models", "A recruitment model trained on past hiring decisions favours one group. What is the most likely cause?",
  ["The historical decisions it learned from contained bias", "The model was trained for too few epochs to converge", "The training data was stored in a columnar file format", "The features were scaled to a mean of zero before training"],
  "A", "Models reproduce patterns, including unfair ones, in their training data; protected characteristics can also leak via proxies.")
q("dashboard-design", "Which TWO choices make a decision-support dashboard more effective?",
  ["Showing the key measures prominently, with targets for context", "Showing trends and comparisons, not isolated single numbers", "Including every available metric so that nothing could be missed", "Using a different chart type for each measure to keep interest"],
  "AB", "Good dashboards are focused and give context; clutter and inconsistency hinder decisions.")
q("storytelling", "When presenting findings to a non-technical board, what is generally the best structure?",
  ["Lead with the key message, then the supporting evidence", "Walk through the method step by step before revealing any results", "Show all the exploratory charts in the order they were produced", "Present the model's technical metrics first to establish credibility"],
  "A", "Answer-first (pyramid) structure respects the audience's time; technical detail goes in an appendix.")
q("colour-accessibility", "Why should a chart not rely on red versus green alone to distinguish categories?",
  ["Colour-blind viewers may be unable to tell them apart", "Red and green print poorly on most office laser printers", "Red and green are reserved for financial data only", "Screen readers announce red and green as the same colour"],
  "A", "About 1 in 12 men have red–green colour vision deficiency; add labels, shapes or accessible palettes.")
q("data-maturity", "An organisation that relies mainly on ad-hoc spreadsheets and individual expertise rather than shared data and governed processes has:",
  ["Low data maturity", "High data maturity", "High data velocity", "Low data veracity"],
  "A", "Data maturity frameworks describe progress from ad-hoc to managed, governed and optimised use of data.")
