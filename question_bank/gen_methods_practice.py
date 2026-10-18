"""General data science revision: methods, experimentation, lifecycle and communication (not assessed KSBs)."""
from ._helpers import make_builder

q, QUESTIONS = make_builder("GEN", "General data science (optional revision beyond the assessed KSBs)", start=101)

# --- Lifecycle -------------------------------------------------------------------------
q("crisp-dm", "Which is the first phase of the CRISP-DM data mining process?",
  ["Business understanding", "Data preparation", "Modelling and tuning", "Deployment to users"],
  "A", "CRISP-DM: business understanding, data understanding, data preparation, modelling, evaluation, deployment.")
q("crisp-dm-order", "In CRISP-DM, which phase comes immediately after data understanding?",
  ["Data preparation", "Evaluation", "Deployment", "Business understanding"],
  "A", "The process is iterative, with frequent loops back to earlier phases.")
q("eda", "What is the main purpose of exploratory data analysis (EDA)?",
  ["To understand the data's structure, quality and patterns before modelling", "To produce the final model that will be deployed into production systems", "To prove the hypothesis the stakeholder expects to be true", "To remove every outlier and missing value from the dataset"],
  "A", "EDA (summary stats, plots, checks) shapes cleaning, features and modelling choices.")
q("problem-framing", "A stakeholder asks for 'an AI model to reduce complaints'. What should a data scientist do first?",
  ["Clarify the decision, success measures and available data", "Train a large language model on all complaint text", "Build a dashboard of every complaint field available", "Choose the most accurate algorithm from a benchmark"],
  "A", "Good problem framing defines the decision to support and how success will be measured.")
q("mvp", "Why deliver a minimum viable product (MVP) of an analytical tool early?",
  ["To get user feedback before investing in a full build", "To avoid needing any testing before release", "To meet the requirement that all tools are free", "To lock in the final design before user research"],
  "A", "Early feedback reduces the risk of building the wrong thing.")
q("data-dictionary", "A document listing each field's name, meaning, type, allowed values and source is a:",
  ["Data dictionary", "Data lake index", "Model card", "Release note"],
  "A", "Data dictionaries make datasets understandable and reduce misinterpretation.")
q("model-card", "A 'model card' documents:",
  ["A model's purpose, performance, limitations and intended use", "The hardware specification of the training server", "The list of team members who wrote the code", "The billing account used for cloud training runs"],
  "A", "Model cards support transparency and appropriate use.")

# --- Experimentation --------------------------------------------------------------------
q("ab-test", "In an A/B test of two letter designs, why are recipients randomly assigned to each version?",
  ["To balance other factors, so differences reflect the design", "To ensure each version is sent to exactly the same number of people", "To let the analyst choose which recipients receive which design", "To make sure the new design performs better than the old one"],
  "A", "Randomisation removes systematic differences between groups.")
q("ab-peeking", "Checking an A/B test's p-value every day and stopping as soon as it drops below 0.05 is a problem because:",
  ["Repeated looks inflate false positives", "Daily checks reduce the effective sample size", "p-values are valid only at the planned end date", "It makes the two groups unequal in size"],
  "A", "Pre-specify sample size or use sequential testing methods designed for interim looks.")
q("power-analysis", "A power analysis before an experiment is used to determine:",
  ["The sample size needed to detect a meaningful effect", "Which variable should be the outcome of interest", "Whether the results will be statistically significant", "How long the analysis code will take to run"],
  "A", "Power depends on effect size, variability, α and sample size.")
q("control-group", "Why does an evaluation of a new intervention need a control or comparison group?",
  ["To estimate what would have happened without the intervention", "To increase the total number of people taking part", "To make the statistical analysis simpler to report to the board", "To ensure everyone eventually receives the intervention"],
  "A", "Without a comparison, changes over time can't be attributed to the intervention.")
q("blinding", "Why are trials sometimes 'blinded' so participants or assessors don't know who received the intervention?",
  ["To reduce bias from expectations influencing outcomes", "To protect participants' names from being published", "To make random allocation unnecessary in the trial", "To allow the sample size to be reduced by half"],
  "A", "Knowledge of assignment can change behaviour or measurement (placebo and observer effects).")
q("observational", "Which TWO methods help estimate causal effects from observational data?",
  ["Propensity score matching", "Instrumental variables", "Increasing the sample size only", "Reporting the raw correlation"],
  "AB", "These methods address confounding under stated assumptions; bigger samples alone don't fix bias.")
q("dag-causal", "In causal inference, a variable that is caused by both the treatment and the outcome is a collider. What happens if you control for it?",
  ["It can create a spurious association", "It removes all confounding bias", "It increases statistical power", "It has no effect on the estimate"],
  "A", "Conditioning on a collider opens a non-causal path (collider bias).")

# --- Statistics & ML extras -----------------------------------------------------------------
q("sampling-methods", "Dividing a population into regions and randomly sampling within each region is:",
  ["Stratified sampling", "Cluster sampling", "Convenience sampling", "Snowball sampling"],
  "A", "Stratified sampling ensures each stratum is represented; cluster sampling samples whole groups.")
q("cluster-sampling", "Randomly selecting 20 schools and surveying every pupil in them is:",
  ["Cluster sampling", "Stratified sampling", "Systematic sampling", "Quota sampling"],
  "A", "Cluster sampling is cheaper but less precise than simple random sampling of the same size.")
q("bias-sampling", "Surveying people who walk past a city-centre office at lunchtime is:",
  ["Convenience sampling", "Stratified sampling", "Random sampling", "Systematic sampling"],
  "A", "Convenience samples are easy but rarely representative.")
q("ols", "Ordinary least squares chooses regression coefficients that minimise:",
  ["The sum of squared residuals", "The sum of absolute residuals", "The number of non-zero coefficients", "The largest single residual"],
  "A", "Least absolute deviations minimises absolute residuals; Lasso adds a coefficient penalty.")
q("dummy-trap", "Including a dummy variable for every category plus an intercept in a linear regression causes:",
  ["Perfect multicollinearity", "Heteroscedasticity", "Autocorrelation of errors", "Overdispersion"],
  "A", "Drop one category as the reference level.")
q("standardise", "Standardising a feature means transforming it to have:",
  ["Mean 0 and standard deviation 1", "Minimum 0 and maximum 1 exactly", "Median 0 and range 1", "Only positive values"],
  "A", "Min–max scaling gives 0–1; standardisation gives z-scores.")
q("feature-engineering", "Which TWO are examples of feature engineering?",
  ["Creating 'days since last purchase' from dates", "Extracting the month from a timestamp", "Choosing the colour scheme of a chart", "Renaming the output file of the model"],
  "AB", "Feature engineering creates informative inputs from raw data.")
q("target-leakage", "A model predicting whether a customer will cancel includes 'date of cancellation email' as a feature. What is wrong?",
  ["It is known only after the outcome", "Dates are unsuitable as model features", "The feature has too many missing values", "It makes the model too simple to be useful"],
  "A", "Features must be available at prediction time.")
q("ensembles-stacking", "Training a meta-model on the predictions of several base models is called:",
  ["Stacking", "Bagging", "Pruning", "Boosting"],
  "A", "Stacking learns how to combine models; bagging averages bootstrap models; boosting adds them sequentially.")
q("curse-dimensionality", "The 'curse of dimensionality' refers to the fact that, as the number of features grows:",
  ["Data become sparse and distances less meaningful", "Models become steadily more accurate as features are added", "Training time decreases with each added feature", "Every feature becomes normally distributed"],
  "A", "High-dimensional spaces need far more data and challenge distance-based methods.")
q("learning-curves", "A learning curve plots training and validation error against training set size. Both errors are high and close together. This suggests:",
  ["High bias: a more flexible model is needed", "High variance: more training data is needed", "Data leakage between the two sets", "The model is perfectly specified"],
  "A", "If both errors are high and converge, more data won't help much; increase model capacity or features.")
q("early-stopping", "Early stopping in model training means:",
  ["Halting when validation performance stops improving", "Stopping after the first epoch to save compute", "Ending training once training loss reaches zero", "Removing the last layer of the network early"],
  "A", "It is a simple, effective regulariser.")
q("association-rules", "Market basket analysis rules such as {bread} → {butter} are evaluated with which TWO measures?",
  ["Support", "Confidence", "Recall", "RMSE"],
  "AB", "Support (how often items co-occur) and confidence (P(butter | bread)); lift compares with independence.")
q("recommender", "A recommender that suggests items liked by users with similar histories uses:",
  ["Collaborative filtering", "Content-based filtering only", "Linear programming", "Principal component regression"],
  "A", "Content-based filtering instead uses item attributes.")
q("spatial-interp", "Estimating air temperature at unmonitored locations from nearby weather stations, weighting closer ones more, is:",
  ["Spatial interpolation", "Temporal aggregation of the station records", "Spatial clustering of the stations with k-means", "Map projection to British National Grid"],
  "A", "IDW and kriging are common spatial interpolation methods.")

# --- Visualisation & communication ------------------------------------------------------------
q("viz-distribution", "Which chart best shows the distribution of a single continuous variable?",
  ["Histogram", "Pie chart", "Stacked bar", "Line chart"],
  "A", "Histograms, density plots and box plots show distributions.")
q("viz-relationship", "Which chart best shows the relationship between two continuous variables?",
  ["Scatter plot", "Pie chart", "Bar chart", "Histogram"],
  "A", "Scatter plots reveal correlation, clusters and outliers.")
q("box-plot", "In a standard box plot, the box spans:",
  ["The interquartile range (Q1 to Q3)", "The mean ± one standard deviation", "The minimum to the maximum", "The 5th to the 95th percentile"],
  "A", "The line inside is the median; whiskers typically extend to 1.5 × IQR.")
q("dual-axis", "Why are dual-axis charts often discouraged?",
  ["Scales can be chosen to suggest misleading relationships", "They are not supported by most plotting libraries", "They only work with categorical data on the x-axis", "They require both series to use the same units"],
  "A", "Two independent scales let a designer make almost any two series look related.")
q("small-multiples", "Showing the same chart for each region in a grid of small panels with shared axes is called:",
  ["Small multiples", "A dual-axis chart", "A treemap layout", "A word cloud grid"],
  "A", "Shared axes make comparisons across panels easy.")
q("accessibility-charts", "Which TWO practices make charts more accessible?",
  ["Adding alt text or a text summary of the key message", "Using direct labels and patterns, not colour alone", "Using light grey text on a white background", "Encoding the key message only in red vs green"],
  "AB", "GOV.UK guidance emphasises text alternatives, contrast and not relying on colour.")
q("plain-english", "When writing for non-specialist decision-makers, which is best practice?",
  ["Plain English, defining technical terms", "Technical terms throughout to show methodological rigour", "Long sentences that include every possible caveat", "Acronyms only, to keep the text short"],
  "A", "Clear writing increases the chance analysis is understood and used.")

# --- Ethics & society ---------------------------------------------------------------------------
q("fairness-metrics", "A model has equal true positive rates across groups. Which fairness criterion does this satisfy?",
  ["Equal opportunity", "Demographic parity", "Calibration within groups", "Individual fairness"],
  "A", "Demographic parity needs equal positive prediction rates; fairness criteria often conflict.")
q("proxy-discrimination", "Removing a protected attribute from a model's inputs may not prevent discrimination because:",
  ["Other features can act as proxies for it", "Models lose accuracy when any feature is removed", "Protected attributes are needed for training", "Removal makes the model more accurate"],
  "A", "Postcode, for example, can correlate with ethnicity; test outcomes across groups.")
q("human-in-loop", "Which TWO situations most call for a human to review a model's output before action is taken?",
  ["Decisions with significant effects on people", "Cases where the model is uncertain", "Routine low-risk sorting of internal team emails", "Spell-checking the analyst's own draft report"],
  "AB", "Human oversight is most important where stakes are high or confidence is low; UK GDPR Article 22 also restricts solely automated significant decisions.")
q("re-identification", "Why can releasing 'anonymised' record-level data still be risky?",
  ["Combining postcode, age and sex can re-identify people", "Anonymised data is encrypted, so it is unusable for analysis", "Record-level data is illegal to publish in every circumstance", "Anonymisation removes too few rows to be statistically useful"],
  "A", "Disclosure control (aggregation, suppression, noise) reduces re-identification risk.")
q("differential-privacy", "Differential privacy protects individuals by:",
  ["Adding calibrated noise so one person's data barely changes outputs", "Encrypting the database with a key held by an independent body", "Deleting every record that contains any personal identifiers", "Requiring signed consent from every person before analysis"],
  "A", "It provides a mathematical privacy guarantee at some cost to accuracy.")
q("environmental-cost", "Which is a recognised environmental concern associated with large AI models?",
  ["Energy and water use for training and running them", "Their tendency to reduce paper consumption in offices", "Their need for physical storage of printed outputs", "Their requirement to run only during daylight hours"],
  "A", "Data centre energy and cooling have notable environmental footprints.")
