from ._helpers import make_builder

q, QUESTIONS = make_builder("5.3", "Common patterns in real-world data")

# --- Missing data ---------------------------------------------------------------------
q("missingness", "High earners are more likely to refuse to report their income in a survey. This missing data is:",
  ["Missing completely at random (MCAR)", "Missing at random (MAR)", "Missing not at random (MNAR)", "Structurally missing"],
  "C", "MNAR: the probability of missingness depends on the unobserved value itself. 'Structurally missing' means the value cannot exist (e.g. pregnancy dates for men).")
q("missingness", "A sensor drops readings because of intermittent radio interference unrelated to the readings or anything else measured. This is:",
  ["MCAR", "MAR", "MNAR", "Censoring"],
  "A", "MCAR: missingness unrelated to any observed or unobserved values.")
q("missingness", "Older respondents are more likely to skip an online question, and age is recorded for everyone. Within each age group, missingness is unrelated to the answer. This is:",
  ["MCAR", "MAR", "MNAR", "Censoring"],
  "B", "MAR: missingness depends on observed variables (age) but not on the missing value itself.")
q("imputation", "What is a known drawback of replacing missing values with the column mean?",
  ["It shrinks variance and weakens relationships", "It inflates the variance and creates new outliers", "It shifts the column mean towards zero", "It changes the number of rows in the data"],
  "A", "Mean imputation reduces spread and ignores relationships; consider multiple imputation or model-based methods.")
q("placeholder-values", "A river level column contains many values of −999. What is the most likely explanation?",
  ["A placeholder code for missing or invalid readings", "A genuine reading taken during an extreme drought", "A reading recorded in feet instead of metres", "A rounding artefact from the logger's firmware"],
  "A", "Sentinel values such as −999, 9999 or 1900-01-01 must be converted to proper missing values before analysis.")

# --- Outliers & anomalies ------------------------------------------------------------------
q("outliers", "A rainfall dataset contains a value five times higher than any other. What should an analyst do first?",
  ["Remove it, as it will distort the summary statistics", "Investigate it with source checks and domain knowledge", "Cap it at the 99th percentile to reduce its influence", "Replace it with the median of the surrounding days"],
  "B", "Outliers can be the most important data (e.g. a flood); investigate before removing, capping or replacing, and document the decision.")
q("anomaly-detection", "Which TWO methods can be used to detect anomalies?",
  ["Z-score or IQR rules", "Isolation Forest", "One-hot encoding", "Min–max scaling"],
  "AB", "Statistical rules and ML methods (Isolation Forest, autoencoders) flag unusual observations; the others are preprocessing steps.")

# --- Distributions -------------------------------------------------------------------------
q("skew", "Which TWO real-world variables are typically right-skewed?",
  ["Household income", "River discharge", "Adult height in one population", "Measurement error of a calibrated gauge"],
  "AB", "Quantities bounded at zero with occasional large values are right-skewed; height and well-behaved measurement error are roughly symmetric.")
q("power-law", "City populations and website traffic often show a few very large values and many small ones. This is characteristic of:",
  ["Heavy-tailed (power-law) distributions", "Uniform (flat) distributions", "Normal (bell-shaped) distributions", "Bimodal (two-peaked) distributions"],
  "A", "Heavy-tailed distributions mean averages can be dominated by a few extreme values.")
q("pareto", "The 'Pareto principle' observation in many datasets is that:",
  ["Roughly 80% of effects come from 20% of causes", "Roughly 95% of values lie within two SDs", "Roughly 30% of leading digits are the digit 1", "Roughly half of values lie above the mean"],
  "A", "e.g. a small share of sites may cause most incidents. The others describe the normal rule and Benford's law.")
q("bimodal", "A histogram of journey times has two distinct peaks. What does this most likely suggest?",
  ["The data combine two different groups or processes", "The data are heavily right-skewed by a few outliers", "The data have been rounded to the nearest 5 minutes", "The sample is too small to show the true shape"],
  "A", "Bimodality often indicates a mixture (e.g. peak and off-peak); consider segmenting the data.")
q("benford", "Benford's law predicts that in many naturally occurring numerical datasets the leading digit is:",
  ["Equally likely to be any digit from 1 to 9", "1 about 30% of the time, with larger digits rarer", "9 about 30% of the time, with smaller digits rarer", "Most likely to be 5, falling away symmetrically"],
  "B", "Deviations from Benford's distribution can flag fabricated or manipulated figures.")
q("zero-inflation", "Daily counts of pollution incidents at a small site are mostly zero with occasional counts. This pattern is called:",
  ["Zero-inflation", "Left-censoring", "Heteroscedasticity", "Seasonality"],
  "A", "Zero-inflated models (e.g. ZIP) handle excess zeros beyond a standard Poisson.")
q("heaping", "Self-reported ages cluster at numbers ending in 0 and 5. This is known as:",
  ["Heaping", "Censoring", "Truncation", "Binning"],
  "A", "Digit preference in reported data creates spikes at round numbers.")

# --- Time and space --------------------------------------------------------------------------
q("seasonality", "Water demand is consistently higher every summer and lower every winter. This is:",
  ["Seasonality", "A cyclical pattern", "A long-term trend", "A structural break"],
  "A", "Seasonality is a regular, calendar-related pattern repeating with a fixed period.")
q("trend-cycle", "How does a cyclical pattern differ from a seasonal pattern?",
  ["Cycles have no fixed period; seasons repeat at a fixed period", "Cycles repeat at a fixed period; seasons have no fixed period", "Cycles only occur in daily data; seasons only in monthly data", "Cycles trend upward over time; seasons rise and fall around a mean"],
  "A", "Seasonal periods are fixed (weekly/annual); cycles (e.g. economic) vary in length.")
q("autocorrelation", "Why should standard random train/test splits be avoided for time-series forecasting?",
  ["Ordering matters, so random splits let the future leak into training", "Time-series data usually has too few rows to split into train and test", "Random splits make the test set larger than the training set", "Time-series models are evaluated on training error instead"],
  "A", "Use time-ordered splits (e.g. rolling-origin / time-series cross-validation).")
q("spatial-autocorrelation", "Nearby monitoring sites tend to record more similar values than distant ones. This is:",
  ["Spatial autocorrelation", "Spatial non-stationarity", "The ecological fallacy", "Edge effects"],
  "A", "Tobler's first law; spatial dependence violates independence assumptions and must be accounted for in modelling and validation.")
q("drift-real-world", "A model trained on pre-pandemic travel data performs poorly afterwards. Which real-world pattern explains this?",
  ["The data-generating process changed (drift)", "The model was evaluated on the training set", "The data contained too many duplicate records", "The data were heaped at round numbers"],
  "A", "Real-world data are non-stationary; models need monitoring and retraining.")
q("structural-break", "A sudden step change in a long-running series coincides with a change in how data were recorded. This is:",
  ["A structural break from a method change", "A seasonal peak in the series", "An outlier caused by a temporary sensor fault", "A cyclical turning point"],
  "A", "Always check metadata for changes in definitions, instruments or processes.")

# --- Data quality patterns --------------------------------------------------------------------
q("duplicates", "Matching records that refer to the same real-world entity across datasets despite spelling differences is called:",
  ["Entity resolution", "Data enrichment", "Schema matching", "Deduplication by key"],
  "A", "Entity resolution / record linkage uses standardisation, blocking and string similarity (e.g. Jaro-Winkler). Schema matching aligns columns, not records.")
q("inconsistent-categories", "A 'town' column contains 'Bristol', 'bristol ', 'BRISTOL' and 'Bristl'. Which TWO cleaning steps are appropriate?",
  ["Standardise case and trim whitespace", "Map variants to a canonical value, with review", "One-hot encode each spelling as its own town", "Drop rows whose town appears fewer than ten times"],
  "AB", "Inconsistent categorical values must be harmonised; encoding or dropping them hides the problem.")
q("class-imbalance", "Which real-world scenario typically produces highly imbalanced classes?",
  ["Detecting rare fraud or pollution events", "Predicting a fair coin toss outcome", "A survey with equal-sized strata by design", "Classifying photos of cats and dogs equally sampled"],
  "A", "Rare events dominate many important problems, requiring suitable metrics and methods.")
q("heteroscedasticity", "In a regression of costs on project size, residuals become much more spread out for larger projects. This is:",
  ["Heteroscedasticity", "Homoscedasticity", "Autocorrelation", "Multicollinearity of predictors"],
  "A", "Non-constant variance; consider transformations or robust standard errors.")
q("multicollinearity-real", "Rainfall over the last 1, 2 and 3 days are used together as predictors and are highly correlated. What problem may arise?",
  ["Unstable, hard-to-interpret coefficients", "Residuals that grow with the fitted values", "Predictions biased towards the mean", "Too few degrees of freedom to fit"],
  "A", "Multicollinearity inflates coefficient variance; the second option is heteroscedasticity.")
q("censoring", "In a study of how long equipment lasts, some units are still working when the study ends, so their failure time is unknown. This is:",
  ["Right-censoring", "Left-truncation", "Missing at random", "Survivorship bias"],
  "A", "Survival methods (e.g. Kaplan–Meier, Cox models) use the partial information from censored units.")
q("hierarchical", "Measurements are taken on pupils who are grouped within schools. Which TWO statements are true?",
  ["Pupils in one school may be more alike, so they aren't independent", "Multilevel models can account for this grouped structure", "Averaging to school level removes any need to model groups", "Standard errors are overstated if the grouping is ignored"],
  "AB", "Clustered data violate independence; ignoring it understates (not overstates) standard errors, and aggregating loses information and risks the ecological fallacy.")
q("measurement-error", "A sensor's readings slowly increase over months even though conditions are stable. This is most likely:",
  ["Calibration drift", "Seasonality", "Concept drift in the data", "Heaping"],
  "A", "Instruments drift and need recalibration; detect with reference checks.")
q("aggregation", "Rates look very different when calculated at regional versus local-authority level, purely because of how boundaries group the data. This is known as:",
  ["The modifiable areal unit problem", "Spatial autocorrelation between areas", "The ecological fallacy", "Simpson's paradox in rates"],
  "A", "MAUP: results of spatial analysis depend on the scale and boundaries of aggregation units. The ecological fallacy is inferring individual behaviour from group data.")
q("survivorship-data", "A dataset of currently active permits is used to estimate average permit duration. What bias may arise?",
  ["Survivorship bias", "Recall bias", "Observer bias", "Measurement bias in records"],
  "A", "Expired or revoked permits are missing (and long-running ones over-represented), distorting the estimate.")
