from ._helpers import make_builder

q, QUESTIONS = make_builder("4.1", "Statistical and mathematical models and methods", start=101)

q("variance-calc", "What is the population variance of the values 2, 4, 6?",
  ["2.67", "4", "2", "8"],
  "A", "Mean = 4; squared deviations 4, 0, 4; sum 8; population variance = 8/3 ≈ 2.67 (sample variance = 8/2 = 4).")
q("sample-variance", "Why does the sample variance formula divide by n − 1 rather than n?",
  ["To correct the bias from estimating the mean from the same sample", "To make the variance larger so that tests are more conservative", "Because one observation is treated as an outlier and excluded", "Because the population size is unknown when sampling"],
  "A", "Bessel's correction makes the sample variance an unbiased estimator of the population variance.")
q("standard-error", "The standard error of the mean is:",
  ["σ / √n", "σ / n", "σ² / n", "√σ / n"],
  "A", "SE = SD / √n: quadrupling the sample size halves the standard error.")
q("sample-size", "To halve the width of a confidence interval for a mean, roughly how must the sample size change?",
  ["Increase it fourfold", "Double it", "Increase it eightfold", "Increase it by half"],
  "A", "Width ∝ 1/√n, so halving the width needs 4× the observations.")
q("percentiles", "A child's height is at the 90th percentile for their age. What does this mean?",
  ["Taller than about 90% of children their age", "90% of the average height for their age", "Shorter than about 90% of children their age", "10% taller than the median child"],
  "A", "The pth percentile is the value below which about p% of observations fall. It says nothing about ratios to the mean or median.")
q("kurtosis", "A distribution with heavier tails and more extreme values than a normal distribution has:",
  ["High (positive excess) kurtosis", "Negative skewness (left tail)", "Low (negative excess) kurtosis", "Zero variance across values"],
  "A", "Kurtosis describes tail heaviness; skewness describes asymmetry.")
q("conditional-probability", "In a group, 40% use public transport and 10% use public transport and cycle. What is P(cycles | uses public transport)?",
  ["0.25", "0.10", "0.40", "0.04"],
  "A", "P(C | T) = P(C and T) / P(T) = 0.10 / 0.40 = 0.25.")
q("mutually-exclusive", "Events A and B are mutually exclusive, with P(A) = 0.3 and P(B) = 0.2. What is P(A or B)?",
  ["0.5", "0.06", "0.44", "0.1"],
  "A", "For mutually exclusive events, P(A ∪ B) = P(A) + P(B). (0.44 would be for independent events: 0.3 + 0.2 − 0.06.)")
q("complement", "The probability that at least one of three independent sensors fails is required. Each fails with probability 0.1. What is it?",
  ["0.271", "0.300", "0.001", "0.729"],
  "A", "P(at least one) = 1 − P(none) = 1 − 0.9³ = 1 − 0.729 = 0.271.")
q("combinations", "How many different teams of 3 can be chosen from 5 analysts (order does not matter)?",
  ["10", "60", "15", "125"],
  "A", "C(5,3) = 5! / (3! × 2!) = 10. Ordered selections would be 5 × 4 × 3 = 60.")
q("law-large-numbers", "As more fair coin tosses are made, the proportion of heads gets closer to 0.5. This is the:",
  ["Law of large numbers", "Central limit theorem", "Gambler's fallacy", "Bayes' theorem"],
  "A", "The LLN concerns convergence of averages; the gambler's fallacy wrongly expects short-run correction.")
q("one-two-tailed", "When is a one-tailed hypothesis test appropriate?",
  ["When only an effect in one specified direction is of interest, decided beforehand", "When the two-tailed result is not significant and a smaller p-value is needed instead", "When the sample size is too small for a two-tailed test to be valid", "When the data are not normally distributed and ranks must be used"],
  "A", "Direction must be specified in advance; switching after seeing data is a form of p-hacking.")
q("paired-test", "Blood pressure is measured for the same 20 patients before and after a treatment. Which test compares the means?",
  ["Paired t-test", "Two-sample t-test", "Chi-squared test", "One-way ANOVA"],
  "A", "Measurements are matched by patient, so the paired test (on the differences) is appropriate.")
q("effect-size", "Cohen's d measures:",
  ["The difference between two means in standard deviation units", "The probability that the null hypothesis is actually true", "The proportion of variance explained by a regression", "The strength of association between categorical variables"],
  "A", "Effect sizes describe magnitude independently of sample size; Cramér's V is for categorical association.")
q("anova-assumptions", "Which TWO are assumptions of one-way ANOVA?",
  ["Observations are independent", "Group variances are roughly equal", "Groups have equal sample sizes", "Data are measured on an ordinal scale"],
  "AB", "ANOVA assumes independence, approximately normal residuals and homogeneity of variance; unequal group sizes are allowed.")
q("normality-test", "Which test is commonly used to check whether a sample is consistent with a normal distribution?",
  ["Shapiro–Wilk", "Kruskal–Wallis", "Mann–Whitney U", "Levene's test"],
  "A", "Levene's tests equal variances; Kruskal–Wallis and Mann–Whitney compare groups. Q-Q plots are a useful visual check.")
q("qq-plot", "On a normal Q-Q plot, points curving away from the line at both ends in an S-shape suggest:",
  ["Heavier or lighter tails than a normal distribution", "Data that are very close to normally distributed", "A strong linear relationship between two variables", "Missing values in the middle of the distribution"],
  "A", "Systematic departures at the ends indicate tail differences; a curve throughout indicates skew.")
q("residual-plot", "A plot of residuals against fitted values shows a clear U-shaped pattern. What does this suggest?",
  ["The relationship is non-linear and the model is mis-specified", "The residuals are independent and normally distributed as required", "The predictors are highly correlated with each other", "The model has been regularised too strongly"],
  "A", "Structure in residuals means the model misses a pattern; consider transformations or polynomial terms.")
q("interaction", "In a regression, an interaction term between advertising spend and region allows:",
  ["The effect of advertising to differ depending on region", "Advertising and region to be removed from the model", "The model to ignore observations with a missing region", "Advertising to be measured on a logarithmic scale"],
  "A", "Interactions model effect modification: one variable's effect depends on another's level.")
q("adjusted-r2", "Why is adjusted R² preferred to R² when comparing models with different numbers of predictors?",
  ["It penalises adding predictors that don't improve the fit enough", "It rises whenever more predictors are added, rewarding complexity", "It measures prediction error in the original units of the outcome", "It tests whether the residuals are normally distributed"],
  "A", "Plain R² never decreases when predictors are added; adjusted R² can, discouraging overfitting.")
q("aic", "When comparing models with AIC (Akaike Information Criterion), which model is preferred?",
  ["The model with the lowest AIC", "The model with the highest AIC", "The model with an AIC closest to 1", "The model with an AIC closest to 0.05"],
  "A", "AIC balances fit and complexity; lower is better. BIC penalises complexity more heavily.")
q("poisson-regression", "Which model is most appropriate for predicting the number of incidents per site per year from site characteristics?",
  ["Poisson (or negative binomial) regression", "Logistic regression with a binary outcome", "Ordinary least squares on raw counts", "K-means clustering of the sites"],
  "A", "Count outcomes suit Poisson GLMs; negative binomial handles overdispersion.")
q("overdispersion", "Count data show a variance much larger than the mean. Which problem does this indicate for a Poisson model?",
  ["Overdispersion", "Underfitting", "Multicollinearity", "Heaping"],
  "A", "Poisson assumes variance = mean; a negative binomial or quasi-Poisson model is more appropriate.")
q("dot-product", "What is the dot product of the vectors [1, 2, 3] and [4, 0, −1]?",
  ["1", "4", "−3", "7"],
  "A", "1×4 + 2×0 + 3×(−1) = 4 + 0 − 3 = 1.")
q("matrix-inverse", "Multiplying a square matrix by its inverse gives:",
  ["The identity matrix", "The zero matrix", "The transpose of the matrix", "The matrix's determinant"],
  "A", "A·A⁻¹ = I. A matrix has an inverse only if its determinant is non-zero.")
q("derivative", "What is the derivative of f(x) = 3x² + 2x with respect to x?",
  ["6x + 2", "3x + 2", "6x² + 2", "x³ + x²"],
  "A", "d/dx(3x²) = 6x and d/dx(2x) = 2. The last option is an antiderivative.")
q("logarithms", "What is log₁₀(1000)?",
  ["3", "10", "100", "30"],
  "A", "10³ = 1000. Log transforms turn multiplicative relationships into additive ones.")
q("moving-average", "Why might a 7-day moving average be applied to daily data?",
  ["To smooth out day-of-week fluctuations and show the underlying trend", "To forecast the next seven days together with a confidence interval", "To remove the long-term trend and leave only seasonality", "To fill missing days with values from the following week"],
  "A", "A centred moving average over the seasonal period removes that cycle, revealing the trend.")
q("exp-smoothing", "Simple exponential smoothing forecasts the next value as:",
  ["A weighted average of past values, with older values weighted less", "The value from exactly one season ago, repeated forward for each step", "A straight line fitted by least squares through all historical observations", "The median of the most recent seven observations"],
  "A", "Holt adds trend and Holt–Winters adds seasonality; the second option is a seasonal naive forecast.")
q("acf", "An autocorrelation function (ACF) plot of monthly data shows a strong spike at lag 12. This suggests:",
  ["Annual seasonality", "A linear trend", "White noise", "A structural break"],
  "A", "Correlation with the value 12 months earlier indicates a yearly cycle.")
q("survival", "The Kaplan–Meier estimator is used to:",
  ["Estimate survival probability over time, allowing for censoring", "Compare the means of three or more independent groups of patients", "Estimate the number of natural clusters in an unlabelled dataset", "Measure agreement between two raters on categorical labels"],
  "A", "It handles units still 'alive' at the end of observation; Cox regression adds covariates.")
