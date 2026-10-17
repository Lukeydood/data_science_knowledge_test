from ._helpers import make_builder

q, QUESTIONS = make_builder("5.3", "Common patterns in real-world data", start=101)

q("missing-indicator", "Before imputing, an analyst adds a column flagging which values were missing. Why?",
  ["Missingness itself may carry information", "It increases the number of rows used", "It removes the need for any further imputation", "It corrects for MNAR data automatically"],
  "A", "Missing indicators let models use the pattern of missingness, which is often informative.")
q("multiple-imputation", "Multiple imputation improves on single imputation mainly because it:",
  ["Reflects uncertainty about the imputed values", "Replaces values with the most common category", "Deletes rows with any missing values first", "Gives unbiased results even for MNAR data"],
  "A", "Several imputed datasets are analysed and combined, so standard errors reflect imputation uncertainty.")
q("listwise-deletion", "Dropping every row with any missing value (listwise deletion) is reasonable mainly when:",
  ["Data are MCAR and few rows are lost", "Data are MNAR and many rows are lost", "Most rows have at least one missing value", "The missing values are all in the target"],
  "A", "Under MCAR deletion is unbiased but loses power; otherwise it can bias results.")
q("forward-fill", "For a river gauge with occasional short gaps, which imputation is often reasonable?",
  ["Interpolating between neighbouring readings", "Replacing gaps with the all-time mean", "Replacing each gap with a zero reading", "Deleting the whole day of data"],
  "A", "Time-series gaps suit interpolation or forward-fill for short gaps; long gaps need more care.")
q("outlier-robust", "Which TWO statistics are robust to outliers?",
  ["Median value", "Interquartile range", "Arithmetic mean", "Range (max − min)"],
  "AB", "The median and IQR depend on ranks; the mean and range are pulled by extremes.")
q("winsorising", "Replacing values above the 99th percentile with the 99th percentile value is called:",
  ["Winsorising", "Normalising", "Bootstrapping", "Smoothing"],
  "A", "Winsorising limits the influence of extremes without deleting records.")
q("mad", "Which robust measure of spread is based on deviations from the median?",
  ["Median absolute deviation (MAD)", "Standard deviation", "Variance of values", "Coefficient of variation"],
  "A", "MAD-based z-scores are a robust alternative for outlier detection.")
q("contextual-anomaly", "A water usage of 500 litres is normal at 7am but highly unusual at 3am. This is a:",
  ["Contextual anomaly", "Global outlier value", "Missing value", "Duplicate record"],
  "A", "Contextual anomalies are unusual only given context such as time of day.")
q("collective-anomaly", "A sensor reports exactly the same value for 48 hours. Each value is plausible, but the run is suspicious. This is a:",
  ["Collective anomaly", "Global outlier", "Seasonal peak", "Heaping effect"],
  "A", "A stuck sensor creates a sequence that is anomalous as a group.")
q("trend-detection", "Which TWO methods can test for a monotonic trend in annual data?",
  ["Mann–Kendall test", "Linear regression on time", "Chi-squared test", "K-means clustering"],
  "AB", "Mann–Kendall is a common non-parametric trend test in environmental science.")
q("seasonal-adjustment", "Why are official statistics such as monthly unemployment often seasonally adjusted?",
  ["To reveal underlying movements beneath regular seasonal patterns", "To remove all random noise and leave only the trend line", "To make the series match a normal distribution exactly", "To convert monthly figures into annual totals automatically"],
  "A", "Seasonal adjustment removes predictable calendar effects so real changes stand out.")
q("calendar-effects", "Which TWO calendar effects commonly affect daily or monthly data?",
  ["Bank holidays", "Varying number of working days", "Leap seconds", "Moon phase names"],
  "AB", "Trading-day and holiday effects distort comparisons unless adjusted for.")
q("non-stationary", "A time series whose mean increases steadily over time is:",
  ["Non-stationary", "Stationary", "White noise", "Uniformly distributed"],
  "A", "Differencing or detrending is often needed before modelling.")
q("random-walk", "Daily share prices often behave like a random walk. What does this imply for forecasting?",
  ["Tomorrow's best forecast is roughly today's value", "Prices return to their long-run mean by the next day", "Prices follow a strong weekly seasonal cycle", "Forecasts improve greatly with complex models"],
  "A", "For random walks the naive forecast is hard to beat.")
q("aggregation-bias", "Monthly averages of hourly flows hide short floods. This illustrates that:",
  ["Aggregation can hide important extremes", "Averages are biased upwards for flow data", "Hourly data contains no useful signal", "Monthly data is more accurate than hourly"],
  "A", "Choose a temporal resolution suited to the question; keep peaks or maxima where they matter.")
q("rounding-precision", "Readings recorded to the nearest 0.5 m produce a histogram with gaps between values. This pattern comes from:",
  ["Limited measurement precision", "A bimodal underlying population", "Missing not at random data", "Concept drift in the sensor"],
  "A", "Coarse recording creates artificial clumping; methods assuming continuous data may need care.")
q("detection-limit", "Water quality results below the lab's limit of detection are reported as '<0.01'. How should they be treated?",
  ["As left-censored values, not zeros or missing", "As zeros, since nothing was detected", "As missing, and deleted from analysis", "As exactly 0.01, with no adjustment or flag"],
  "A", "Censored-data methods (or substitution with sensitivity checks) avoid bias.")
q("unit-inconsistency", "A combined dataset shows flows around 2 for some sites and 2000 for others. Which TWO explanations should be checked first?",
  ["Different units, e.g. m³/s vs l/s", "Different scaling or recording conventions", "A genuine thousandfold difference in flow", "Random sampling noise between sites"],
  "AB", "Unit and convention mismatches are common when merging sources.")
q("duplicates-time", "A telemetry feed occasionally sends the same reading twice with identical timestamps. What is the best cleaning rule?",
  ["Remove exact duplicates on site and timestamp", "Average every pair of consecutive readings", "Delete every reading from the affected days", "Keep duplicates to increase the sample size"],
  "A", "Define a natural key (site + time) and de-duplicate, logging how many were removed.")
q("free-text-variation", "A free-text 'cause' field contains 'blockage', 'blocked pipe', 'Blockage - debris'. What pattern is this?",
  ["Inconsistent free text", "Missing at random values", "Seasonal variation", "Spatial autocorrelation"],
  "A", "Map free text to controlled categories (rules, fuzzy matching or NLP) and improve data entry.")
q("correlation-time", "Two variables that both rise over ten years show a high correlation. Why should this be treated cautiously?",
  ["Shared trends can create spurious correlation", "Correlation needs at least 1,000 data points", "Rising variables are excluded from correlation tests", "Correlation is only valid for categories"],
  "A", "Detrend or difference series before inferring a relationship.")
q("long-tail-categories", "A categorical variable has 500 levels, most appearing only a few times. Which TWO approaches help?",
  ["Group rare levels into an 'Other' category", "Use target or frequency encoding carefully", "One-hot encode all 500 levels for a small dataset", "Delete the variable without assessment"],
  "AB", "High cardinality causes sparsity and overfitting; group or encode with care (avoiding leakage).")
q("sample-selection", "A model trained on reported incidents is used to predict where incidents occur. Why could this be biased?",
  ["Reporting depends on who notices and reports", "Incidents are reported immediately in most systems", "Reported data has no locations recorded", "Models are unable to use count data as a target"],
  "A", "Areas with fewer observers may look safer than they are; reporting bias is common.")
q("data-collection-change", "After a new app makes reporting easier, recorded incidents rise sharply. What is the most likely explanation?",
  ["A change in recording, not in incidents", "A real tripling of the underlying incident rate", "Regression to the mean in incident rates", "A seasonal effect repeating each year"],
  "A", "Changes in process alter what is captured; check metadata before concluding real change.")
q("survivorship-model", "A failure-prediction model is trained only on assets still in service. Which pattern biases it?",
  ["Survivorship bias", "Seasonality in failures", "Heaping at round values", "Zero-inflation"],
  "A", "Assets that already failed are excluded, so risk factors are under-represented.")
q("feedback-loop", "A model directs inspections to high-risk sites, and new training data comes only from inspected sites. What risk arises?",
  ["A feedback loop reinforcing the model's own biases", "The model becomes more accurate on every site", "The data becomes missing completely at random", "Inspections reduce the number of features available"],
  "A", "Data generated by the model's decisions can entrench errors; reserve some random checks.")
