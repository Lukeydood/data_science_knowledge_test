from ._helpers import make_builder

q, QUESTIONS = make_builder("3.3", "Data-driven decision making and the good use of evidence and analytics")

# --- Causation & evidence -------------------------------------------------------
q("correlation-causation", "Towns with more coffee shops have higher house prices. An investor concludes that opening more coffee shops will push house prices up. What is the main flaw?",
  ["The sample of areas is too small to detect an effect", "An association alone does not show the shops cause the rise", "The correlation should have been tested for normality first", "Shop numbers are counts, so Spearman should be used"],
  "B", "Observational association may reflect confounding (e.g. local incomes) or reverse causation; causal claims need experimental or quasi-experimental evidence.")
q("confounding", "Ice-cream sales and drowning incidents are positively correlated. What is the most likely explanation?",
  ["Reverse causation from drownings to sales", "A third variable, hot weather, drives both", "Measurement error in the drowning records", "Regression to the mean in both series"],
  "B", "A confounder influences both variables, creating a spurious association.")
q("rct", "What is generally considered the strongest single-study design for establishing that an intervention causes an outcome?",
  ["Prospective cohort study", "Case-control study", "Randomised controlled trial", "Interrupted time series"],
  "C", "Random assignment balances known and unknown confounders between groups; the others are useful but more vulnerable to bias.")
q("evidence-hierarchy", "In a typical hierarchy of evidence, which sits at the top?",
  ["Systematic reviews of well-conducted RCTs", "A single large randomised controlled trial", "Large, well-designed observational cohorts", "Consensus statements from expert panels"],
  "A", "Syntheses of multiple high-quality studies reduce the influence of chance and bias in any one study.")
q("quasi-experiment", "A policy is introduced in one region but not a similar neighbouring region. Comparing the change over time in both regions estimates the policy effect. Which method is this?",
  ["Difference-in-differences", "Regression discontinuity", "Propensity score matching", "Instrumental variables"],
  "A", "Difference-in-differences uses a comparison group's trend as the counterfactual, assuming parallel trends.")
q("counterfactual", "When evaluating whether a customer loyalty campaign worked, why is a counterfactual needed?",
  ["To estimate what would have happened without the campaign", "To compare the campaign's cost with its planned budget", "To check the outcome data were collected consistently", "To identify which groups the campaign failed to reach"],
  "A", "Impact = outcome with intervention minus outcome without it; the counterfactual is the 'without' estimate.")

# --- Biases & fallacies ------------------------------------------------------------
q("confirmation-bias", "An analyst searches only for evidence supporting the option their director already prefers. This is:",
  ["Survivorship bias", "Confirmation bias", "Anchoring bias", "Selection bias"],
  "B", "Confirmation bias is favouring information that confirms existing beliefs.")
q("survivorship-bias", "Analysing only businesses that are still trading to find 'the secrets of success' risks which bias?",
  ["Survivorship bias", "Anchoring bias", "Recall bias", "Observer bias"],
  "A", "Excluding failures (non-survivors) hides factors shared by both groups and overstates success factors.")
q("anchoring", "Stakeholders estimate a project cost after first hearing an unrelated high figure, and their estimates are skewed upward. This is:",
  ["Anchoring bias", "Availability bias", "Optimism bias", "Hindsight bias"],
  "A", "Anchoring is over-reliance on the first piece of information encountered.")
q("availability", "After a high-profile data breach is in the news, a team overestimates how often such breaches occur. This reflects:",
  ["Availability bias", "Anchoring bias", "Confirmation bias", "Optimism bias"],
  "A", "Availability bias judges frequency by how easily examples come to mind.")
q("selection-bias", "An online survey about broadband access is used to estimate national internet usage. What is the main concern?",
  ["People without internet access cannot take part", "Online responses are harder to code and analyse", "Respondents may misremember their past usage", "Questions may be interpreted in different ways"],
  "A", "The sampling frame excludes the very group of interest (selection bias), so the estimate is biased upward.")
q("simpsons-paradox", "A treatment appears better in each of two hospitals separately, but worse when the data are combined. This is an example of:",
  ["Simpson's paradox", "Regression to the mean", "Ecological fallacy", "Berkson's paradox"],
  "A", "Simpson's paradox: a trend in subgroups reverses when aggregated, usually because a confounder is unevenly distributed.")
q("goodharts-law", "A target to 'close 95% of complaints within 5 days' leads staff to close complaints prematurely. Which principle does this illustrate?",
  ["Goodhart's law", "Parkinson's law", "Benford's law", "Pareto principle"],
  "A", "Goodhart's law: when a measure becomes a target, it ceases to be a good measure, because people optimise the metric.")
q("regression-to-mean", "Speed cameras are installed at sites that had unusually high accident numbers last year; accidents fall the next year. Why should this be interpreted with caution?",
  ["Extreme years tend to be followed by more typical ones anyway", "Drivers may divert to other roads, moving the accidents", "Accident reporting may have changed when cameras arrived", "One year of follow-up data is too short to be significant"],
  "A", "Regression to the mean: sites selected for extreme values would likely improve anyway; a comparison group is needed. The other points are real concerns but are not the core statistical issue here.")
q("base-rate", "A test for a rare condition is 95% accurate. A decision-maker assumes a positive result means a 95% chance of having the condition. Which error is this?",
  ["Base rate neglect", "Gambler's fallacy", "Survivorship bias", "Ecological fallacy"],
  "A", "When prevalence is low, most positives can be false positives; the base rate must be considered.")
q("p-hacking", "Which TWO practices undermine the integrity of evidence?",
  ["Running many analyses and reporting only the significant ones", "Pre-registering the analysis plan before seeing the data", "Choosing the time period after seeing which supports the case", "Publishing the code and data so others can check the results"],
  "AC", "P-hacking and cherry-picking inflate false findings; pre-registration and openness protect against them.")

# --- Significance & uncertainty ------------------------------------------------------
q("practical-significance", "With 5 million records, a difference of 0.01% between two groups is statistically significant (p < 0.001). What should a decision-maker conclude?",
  ["The difference is real and large enough to act on", "The effect may be too small to matter in practice", "The test is invalid because the sample is too large", "The low p-value shows the groups differ causally"],
  "B", "Large samples make tiny effects significant; always consider effect size and context.")
q("communicating-uncertainty", "Which is the best way to communicate a model's forecast to senior decision-makers?",
  ["A single precise figure, so the message is clear", "A central estimate with a range and key assumptions", "The best and worst cases, without a central estimate", "The model's accuracy score on its training data"],
  "B", "Good practice conveys uncertainty honestly, avoids false precision, and states assumptions.")
q("expected-value", "Option A has a 50% chance of saving £100k and 50% chance of saving nothing. Option B saves £40k for certain. What is the expected value of option A?",
  ["£40k", "£50k", "£100k", "£60k"],
  "B", "EV = 0.5 × £100k + 0.5 × £0 = £50k. Risk appetite may still favour the certain option.")

# --- Analytics types & data quality -------------------------------------------------
q("analytics-types", "A model that recommends the optimal allocation of maintenance crews is an example of which type of analytics?",
  ["Descriptive", "Diagnostic", "Predictive", "Prescriptive"],
  "D", "Prescriptive analytics answers 'what should we do?', often using optimisation or simulation.")
q("analytics-types", "Investigating why customer complaints rose last quarter is which type of analytics?",
  ["Descriptive", "Diagnostic", "Predictive", "Prescriptive"],
  "B", "Diagnostic analytics answers 'why did it happen?'.")
q("analytics-types", "Forecasting next month's sales from historical data is which type of analytics?",
  ["Descriptive", "Diagnostic", "Predictive", "Prescriptive"],
  "C", "Predictive analytics answers 'what is likely to happen?'.")
q("data-quality", "30% of incident records have no postcode. Which data quality dimension is affected?",
  ["Timeliness", "Completeness", "Uniqueness", "Validity"],
  "B", "Completeness measures whether all required data is present. Validity would be a postcode in the wrong format.")
q("data-quality", "Monitoring data arrives three weeks after the readings were taken, too late for operational decisions. Which data quality dimension is affected?",
  ["Accuracy", "Timeliness", "Validity", "Consistency"],
  "B", "Timeliness is whether data is available when needed.")
q("data-quality", "The same customer appears three times in a CRM with slightly different spellings. Which data quality dimension is affected?",
  ["Uniqueness", "Timeliness", "Completeness", "Validity"],
  "A", "Uniqueness means each real-world entity is recorded once.")

# --- UK government frameworks & ethics ----------------------------------------------
q("five-safes", "The 'Five Safes' framework for providing access to sensitive data consists of:",
  ["Safe people, projects, settings, data and outputs", "Safe storage, access, transfer, retention and disposal", "Safe collection, consent, purpose, accuracy and security", "Safe models, metrics, monitoring, review and release"],
  "A", "The Five Safes (used by ONS and others) assess access to confidential data across people, projects, settings, data and outputs.")
q("gdpr-principles", "Collecting only the personal data that is necessary for the stated purpose is which UK GDPR principle?",
  ["Data minimisation", "Storage limitation", "Purpose limitation", "Accuracy"],
  "A", "Data minimisation: adequate, relevant and limited to what is necessary. Purpose limitation is about not reusing data for incompatible purposes.")
q("gdpr-principles", "Which TWO are principles of UK GDPR?",
  ["Purpose limitation", "Storage limitation", "Proportional retention", "Legitimate reuse"],
  "AB", "The principles are lawfulness/fairness/transparency, purpose limitation, data minimisation, accuracy, storage limitation, integrity/confidentiality and accountability.")
q("dpia", "When is a Data Protection Impact Assessment (DPIA) required under UK GDPR?",
  ["When any personal data is processed for a new project", "When processing is likely to be high risk to individuals", "When personal data is transferred to another UK body", "When the data subject requests a copy of their data"],
  "B", "DPIAs are mandatory for likely high-risk processing, e.g. large-scale special category data or systematic monitoring.")
q("data-ethics", "The UK Government Data Ethics Framework's overarching principles are:",
  ["Transparency, accountability and fairness", "Accuracy, completeness and timeliness", "Lawfulness, consent and minimisation", "Security, availability and integrity"],
  "A", "The framework centres on transparency, accountability and fairness. The others are data-quality, GDPR-style and security properties.")

# --- Visualisation for decisions -------------------------------------------------------
q("chart-choice", "Which chart is most appropriate for showing how a monthly measurement changes over three years?",
  ["Line chart", "Stacked bar chart", "Scatter plot", "Pie chart"],
  "A", "Line charts show trends over continuous time.")
q("chart-choice", "Which chart is most appropriate for comparing the number of incidents across eight regions?",
  ["Bar chart", "Pie chart", "Line chart", "Area chart"],
  "A", "Bar charts make comparisons across categories easy because lengths share a common baseline; lines imply a continuous sequence.")
q("chart-integrity", "A bar chart's y-axis starts at 95 rather than 0, making a 2% difference look huge. What is the problem?",
  ["The axis exaggerates the difference between bars", "The bars should be ordered from largest to smallest", "The chart should use a logarithmic scale instead", "The values should be shown as a stacked total"],
  "A", "Bar lengths encode magnitude, so bar charts should start at zero.")
