from ._helpers import make_builder

q, QUESTIONS = make_builder("4.1", "Statistical and mathematical models and methods")

# --- Descriptive statistics -----------------------------------------------------
q("central-tendency", "Household income is strongly right-skewed. Which measure of central tendency best represents a 'typical' household?",
  ["Mean", "Median", "Mode", "Midrange"],
  "B", "The median is robust to extreme values; the mean and midrange are pulled toward the long tail, and the mode is unstable for continuous data.")
q("central-tendency", "In a right-skewed (positively skewed) distribution, what is the usual relationship between mean and median?",
  ["Mean is less than median", "Mean is greater than median", "Mean equals the median", "Median equals the mode"],
  "B", "The long right tail pulls the mean above the median.")
q("spread", "What does the standard deviation measure?",
  ["The typical distance of values from the mean", "The range covered by the middle half of the data", "The average of the squared deviations from the mean", "The uncertainty in the estimate of the sample mean"],
  "A", "SD is the square root of the variance (third option). The IQR is the middle half; the standard error is the uncertainty in the mean.")
q("iqr-outliers", "Using the common Tukey rule, a value is flagged as an outlier if it lies:",
  ["More than 1.5 × IQR below Q1 or above Q3", "More than 1.5 standard deviations from the mean", "More than 2 × IQR from the median", "Outside the 5th to 95th percentile range"],
  "A", "Tukey's fences are Q1 − 1.5×IQR and Q3 + 1.5×IQR.")
q("normal-rule", "For a normal distribution, approximately what percentage of values lie within ±2 standard deviations of the mean?",
  ["68%", "95%", "99.7%", "90%"],
  "B", "Empirical rule: ~68% within 1 SD, ~95% within 2 SD, ~99.7% within 3 SD.")
q("z-score", "A reading has a z-score of −2.5. What does this mean?",
  ["It is 2.5 units below the mean", "It is 2.5 standard deviations below the mean", "It is at the 2.5th percentile", "It is 2.5 standard errors below the mean"],
  "B", "z = (x − mean) / SD, measuring distance from the mean in standard deviations.")
q("expected-value-dice", "What is the expected value of a single roll of a fair six-sided die?",
  ["3", "3.5", "4", "2.5"],
  "B", "(1+2+3+4+5+6)/6 = 21/6 = 3.5.")

# --- Probability ----------------------------------------------------------------
q("independence", "Events A and B are independent if and only if:",
  ["P(A and B) = P(A) + P(B)", "P(A and B) = P(A) × P(B)", "P(A or B) = P(A) + P(B)", "P(A | B) = P(B | A)"],
  "B", "Independence: P(A∩B) = P(A)P(B). P(A or B) = P(A)+P(B) describes mutually exclusive events.")
q("bayes", "A disease affects 1% of people. A test has 99% sensitivity and 95% specificity. Approximately what is the probability a person who tests positive actually has the disease?",
  ["99%", "95%", "17%", "5%"],
  "C", "P(D|+) = (0.99×0.01)/(0.99×0.01 + 0.05×0.99) = 0.0099/0.0594 ≈ 0.167. Low prevalence means many positives are false.")
q("bayes", "In Bayesian inference, what is the posterior distribution?",
  ["The belief about parameters before seeing any data", "The updated belief after combining prior and likelihood", "The probability of the data given the parameters", "The distribution of the statistic over repeated samples"],
  "B", "Posterior ∝ likelihood × prior. The first option is the prior, the third the likelihood, the fourth a sampling distribution.")
q("distributions", "The number of pollution incidents reported per week, where incidents occur independently at a constant average rate, is best modelled by which distribution?",
  ["Normal", "Poisson", "Exponential", "Binomial"],
  "B", "Poisson models counts of independent events in a fixed interval. Exponential models the time between them.")
q("distributions", "The number of successful outcomes in 20 independent trials, each with the same probability of success, follows which distribution?",
  ["Binomial", "Poisson", "Geometric", "Uniform"],
  "A", "Binomial(n, p) models successes in n independent trials. Geometric models trials until the first success.")
q("distributions", "The waiting time between independent random events occurring at a constant rate follows which distribution?",
  ["Exponential", "Poisson", "Normal", "Binomial"],
  "A", "Inter-arrival times of a Poisson process are exponentially distributed.")
q("clt", "What does the Central Limit Theorem state?",
  ["Large samples from any population are approximately normal", "The distribution of sample means tends to normal as n grows", "The sample mean converges to the population mean as n grows", "Sample variance shrinks towards zero as n grows large"],
  "B", "The CLT is about the sampling distribution of the mean (given finite variance). The third option is the law of large numbers; the data themselves don't become normal.")

# --- Inference --------------------------------------------------------------------
q("p-value", "What is the correct interpretation of a p-value of 0.03?",
  ["A 3% probability that the null hypothesis is true", "A 3% chance of data this extreme if the null were true", "A 97% probability that the alternative is true", "A 3% probability the result is due to sampling error"],
  "B", "A p-value is computed assuming H0 is true; it is not the probability that H0 (or chance alone) explains the result.")
q("errors", "A Type I error is:",
  ["Failing to reject a false null hypothesis", "Rejecting a true null hypothesis", "Accepting a false alternative hypothesis", "Using a one-tailed test by mistake"],
  "B", "Type I = false positive (probability α); Type II = false negative (probability β).")
q("errors", "Which TWO actions typically increase the statistical power of a test?",
  ["Increasing the sample size", "Studying a larger true effect", "Lowering α from 0.05 to 0.01", "Using a two-tailed test instead"],
  "AB", "Power rises with sample size and effect size; a stricter α or a two-tailed (vs one-tailed) test reduces power.")
q("confidence-interval", "Which is the correct interpretation of a 95% confidence interval?",
  ["There is a 95% probability the true value is in this interval", "95% of intervals built this way would contain the true value", "95% of the observed data values lie within this interval", "A repeat study has a 95% chance of a mean in this interval"],
  "B", "Confidence refers to the long-run performance of the method (frequentist interpretation).")
q("test-choice", "Which test is appropriate for comparing the mean of a continuous, roughly normal variable between two independent groups?",
  ["Paired t-test", "Two-sample t-test", "Chi-squared test", "One-sample t-test"],
  "B", "A two-sample t-test compares means of two independent groups; paired t-tests are for matched observations.")
q("test-choice", "Which test is appropriate for assessing whether two categorical variables (e.g. region and incident type) are associated?",
  ["Chi-squared test", "One-way ANOVA", "Pearson correlation", "Two-sample t-test"],
  "A", "The chi-squared test of independence compares observed and expected counts in a contingency table.")
q("test-choice", "Which test compares means across three or more independent groups?",
  ["One-way ANOVA", "Chi-squared test", "Paired t-test", "Fisher's exact test"],
  "A", "ANOVA tests whether at least one group mean differs; post-hoc tests identify which.")
q("test-choice", "Two independent groups have heavily skewed data and small samples. Which non-parametric test could replace the two-sample t-test?",
  ["Mann–Whitney U test", "Wilcoxon signed-rank test", "Kruskal–Wallis test", "Shapiro–Wilk test"],
  "A", "Mann–Whitney U compares two independent groups by ranks. Signed-rank is for paired data, Kruskal–Wallis for 3+ groups, Shapiro–Wilk tests normality.")
q("correlation", "When is Spearman's rank correlation preferred over Pearson's correlation?",
  ["When the relationship is monotonic but not linear", "When both variables are continuous and normal", "When one variable is binary and one continuous", "When the sample is very large and linear"],
  "A", "Spearman measures monotonic association using ranks (also suits ordinal data and outliers); Pearson measures linear association.")
q("multiple-testing", "An analyst runs 20 independent hypothesis tests at α = 0.05. Using a Bonferroni correction, what significance threshold should each test use?",
  ["0.05", "0.025", "0.0025", "0.01"],
  "C", "Bonferroni: α / m = 0.05 / 20 = 0.0025, controlling the family-wise error rate.")
q("bootstrap", "Bootstrapping estimates the uncertainty of a statistic by:",
  ["Resampling the observed data with replacement many times", "Splitting the data into k folds and averaging the results", "Drawing new samples from a fitted normal distribution", "Leaving out one observation at a time and refitting"],
  "A", "The spread of the statistic across bootstrap resamples approximates its sampling distribution. Leave-one-out is the jackknife; k folds is cross-validation.")

# --- Regression -----------------------------------------------------------------
q("regression-assumptions", "Which TWO are assumptions of ordinary least squares linear regression?",
  ["Residuals have constant variance", "Residuals are independent of each other", "Predictors are normally distributed", "The outcome is normally distributed"],
  "AB", "Key assumptions: linearity, independent errors, homoscedasticity and (for inference) normally distributed residuals. Predictors need not be normal.")
q("r-squared", "A regression model has R² = 0.72. What does this mean?",
  ["72% of predictions fall within one standard error", "72% of the variance in the outcome is explained", "The correlation between predictor and outcome is 0.72", "The model's coefficients are 72% likely to be correct"],
  "B", "R² is the proportion of outcome variance explained. (For one predictor the correlation would be √0.72 ≈ 0.85.)")
q("multicollinearity", "Which statistic is commonly used to detect multicollinearity between predictors in a regression?",
  ["Variance inflation factor", "Adjusted R-squared", "Durbin–Watson statistic", "Cook's distance"],
  "A", "High VIF indicates a predictor is largely explained by the others. Durbin–Watson tests autocorrelation; Cook's distance finds influential points.")
q("logistic", "In logistic regression, exponentiating a coefficient gives:",
  ["The change in probability for a one-unit increase", "The odds ratio for a one-unit increase in that predictor", "The change in log-odds for a one-unit increase", "The predicted probability when the predictor is zero"],
  "B", "Logistic regression models log-odds (the raw coefficient); exp(β) is the multiplicative change in odds.")
q("log-transform", "Why might you apply a log transform to a strongly right-skewed variable such as property value?",
  ["To reduce skew and make relationships closer to linear", "To remove extreme values from the dataset", "To standardise the variable to mean 0 and SD 1", "To convert the values into ordered categories"],
  "A", "Log transforms compress large values, reducing skew and stabilising variance; outliers remain, just less extreme.")

# --- Linear algebra, calculus, time series -------------------------------------------
q("matrix-dims", "Multiplying a 3 × 2 matrix by a 2 × 4 matrix produces a matrix of what size?",
  ["2 × 2", "3 × 4", "4 × 3", "2 × 4"],
  "B", "(m×n)(n×p) = m×p; inner dimensions must match.")
q("pca-eigen", "In Principal Component Analysis (PCA), what do the eigenvectors of the covariance matrix represent?",
  ["The directions of maximum variance in the data", "The amount of variance each component explains", "The centres of the natural clusters in the data", "The loadings of each observation on the outcome"],
  "A", "Eigenvectors give component directions; the eigenvalues (second option) give the variance each explains.")
q("gradient-descent", "In gradient descent, parameters are updated by moving:",
  ["In the direction of the gradient", "Against the direction of the gradient", "Perpendicular to the gradient", "Towards the mean of the parameters"],
  "B", "θ ← θ − η∇L(θ): stepping against the gradient decreases the loss.")
q("time-series", "Which TWO are standard components when decomposing a time series?",
  ["Trend", "Seasonality", "Autocorrelation", "Stationarity"],
  "AB", "Classical decomposition splits a series into trend, seasonal and residual components. Autocorrelation and stationarity are properties, not components.")
q("stationarity", "In an ARIMA(p, d, q) model, what does the 'd' parameter represent?",
  ["The number of autoregressive lag terms", "The number of times the series is differenced", "The number of lagged forecast-error terms", "The length of the seasonal period"],
  "B", "d is the order of differencing; p is AR order and q is MA order.")
