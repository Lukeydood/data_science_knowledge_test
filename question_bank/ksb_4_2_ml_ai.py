from ._helpers import make_builder

q, QUESTIONS = make_builder("4.2", "Advanced and predictive analytics, machine learning and AI, simulation, optimisation and automation")

# --- Learning paradigms ----------------------------------------------------------
q("learning-types", "Grouping customers into segments when no labels exist is an example of:",
  ["Supervised learning", "Unsupervised learning", "Reinforcement learning", "Semi-supervised learning"],
  "B", "Clustering finds structure in unlabelled data.")
q("learning-types", "An agent learns to control pump schedules by trial and error, receiving rewards for lower energy use while meeting demand. This is:",
  ["Reinforcement learning", "Unsupervised learning", "Supervised learning", "Transfer learning"],
  "A", "Reinforcement learning optimises actions through rewards from interacting with an environment.")
q("task-type", "Predicting the price a house will sell for is a:",
  ["Classification problem", "Regression problem", "Clustering problem", "Ranking problem"],
  "B", "Regression predicts a continuous numeric target.")
q("task-type", "Predicting whether an email is spam or not is a:",
  ["Binary classification problem", "Regression problem", "Clustering problem", "Anomaly detection problem"],
  "A", "The target has two labelled classes. Anomaly detection is usually used when labels are not available.")

# --- Generalisation ---------------------------------------------------------------
q("overfitting", "A model scores 99% accuracy on training data but 70% on the test set. What is the most likely issue?",
  ["Underfitting", "Overfitting", "Class imbalance", "Concept drift"],
  "B", "A large gap between training and test performance indicates the model has learned noise in the training set.")
q("overfitting", "Which TWO actions typically reduce overfitting?",
  ["Adding regularisation such as L2 or dropout", "Gathering more representative training data", "Adding more layers and training for longer", "Removing the validation set to train on more data"],
  "AB", "Regularisation and more data improve generalisation; more capacity and no validation make overfitting worse or invisible.")
q("bias-variance", "A very simple linear model performs poorly on both training and test data. It most likely has:",
  ["High variance", "High bias", "Data leakage", "Low bias"],
  "B", "High bias = too simple to capture the pattern (underfitting); high variance = too sensitive to the training data.")
q("regularisation", "Which regularisation method can shrink some coefficients exactly to zero, effectively performing feature selection?",
  ["L1 (Lasso)", "L2 (Ridge)", "Dropout", "Early stopping"],
  "A", "The L1 penalty produces sparse solutions; L2 shrinks coefficients but rarely to exactly zero.")
q("cross-validation", "What is the main purpose of k-fold cross-validation?",
  ["To enlarge the training set by creating resampled copies", "To get a more reliable estimate of out-of-sample performance", "To balance the classes in each fold before training", "To reduce training time by fitting on smaller subsets"],
  "B", "Each observation is used for validation once, reducing dependence on a single split.")
q("data-leakage", "Which TWO are examples of data leakage?",
  ["Fitting a scaler on all data before the train/test split", "Randomly shuffling time series so the future predicts the past", "Fitting preprocessing inside a pipeline on training folds", "Holding back a test set until the final evaluation"],
  "AB", "Leakage lets test-set or future information into training, giving over-optimistic results.")
q("hyperparameters", "Which of these is a hyperparameter rather than a learned model parameter?",
  ["The weights of a neural network", "The coefficients of a linear regression", "The maximum depth of a decision tree", "The split thresholds in a decision tree"],
  "C", "Hyperparameters are set before training (and tuned); parameters are learned from data.")
q("tuning", "Why can random search be more efficient than grid search for hyperparameter tuning?",
  ["It tries more distinct values of each important hyperparameter", "It uses earlier results to choose the next values to try", "It evaluates every combination in fewer total model fits", "It removes the need for a separate validation set"],
  "A", "When only some hyperparameters matter, random sampling explores more of their values. Using earlier results describes Bayesian optimisation.")

# --- Evaluation --------------------------------------------------------------------
q("precision-recall", "A classifier gives TP = 40, FP = 10, FN = 20. What is its precision?",
  ["0.67", "0.80", "0.57", "0.75"],
  "B", "Precision = TP / (TP + FP) = 40 / 50 = 0.80.")
q("precision-recall", "A classifier gives TP = 40, FP = 10, FN = 20. What is its recall?",
  ["0.67", "0.80", "0.57", "0.33"],
  "A", "Recall = TP / (TP + FN) = 40 / 60 ≈ 0.67.")
q("precision-recall", "For a cancer screening classifier, missing a real case is far more costly than a false alarm. Which metric should be prioritised?",
  ["Precision", "Recall", "Specificity", "Accuracy"],
  "B", "Recall (sensitivity) is the share of actual positives detected; maximising it minimises false negatives.")
q("imbalance", "Only 1% of transactions are fraudulent. A model predicting 'not fraud' for everything achieves 99% accuracy. Which TWO responses are appropriate?",
  ["Evaluate with precision, recall or PR-AUC", "Use resampling or class weights in training", "Report accuracy, as 99% exceeds the target", "Tune the threshold to maximise accuracy"],
  "AB", "Accuracy is misleading under class imbalance; use suitable metrics and rebalancing techniques.")
q("roc-auc", "A classifier has ROC AUC = 0.5. What does this indicate?",
  ["It ranks positives no better than chance", "It is correct on half of all predictions", "It has a precision of 50% on positives", "It finds half of the actual positives"],
  "A", "AUC is the probability a random positive is ranked above a random negative; 0.5 equals chance.")
q("regression-metrics", "Which regression metric penalises large errors more heavily because errors are squared?",
  ["Mean absolute error", "Root mean squared error", "Median absolute error", "Mean absolute percentage error"],
  "B", "Squaring makes RMSE sensitive to large errors; MAE and median AE treat errors linearly.")

# --- Algorithms ----------------------------------------------------------------------
q("random-forest", "How does a random forest reduce variance compared with a single decision tree?",
  ["Averaging many trees fit on bootstrap samples and random features", "Fitting trees in sequence, each correcting the last one's errors", "Pruning a single deep tree back using cross-validation", "Weighting each training example by how often it is misclassified"],
  "A", "Bagging plus feature randomness decorrelates trees; averaging reduces variance. Sequential correction is boosting.")
q("boosting", "Gradient boosting (e.g. XGBoost, LightGBM) builds an ensemble by:",
  ["Training trees independently in parallel and averaging them", "Adding models in sequence, each fitting the current errors", "Training one deep tree and pruning it with a validation set", "Training models on different feature subsets and voting"],
  "B", "Boosting reduces bias by sequentially fitting residual errors.")
q("kmeans", "Which TWO statements about k-means clustering are true?",
  ["The number of clusters k is chosen in advance", "Results are sensitive to the scale of features", "It finds clusters of arbitrary, non-convex shape", "It labels low-density points as noise"],
  "AB", "k-means needs k up front and uses Euclidean distance, so scale matters; arbitrary shapes and noise labels are DBSCAN features.")
q("kmeans", "The 'elbow method' is used to:",
  ["Choose a suitable number of clusters", "Choose a suitable learning rate", "Choose a probability threshold", "Choose the number of PCA features"],
  "A", "Plot within-cluster sum of squares against k and look for the point of diminishing returns. (A similar 'scree plot' is used for PCA.)")
q("dbscan", "An advantage of DBSCAN over k-means is that DBSCAN:",
  ["Scales better to very high-dimensional data", "Finds arbitrarily shaped clusters and flags noise", "Produces the same clusters regardless of parameters", "Assigns every point to exactly one cluster"],
  "B", "DBSCAN groups dense regions, does not need k, and labels sparse points as noise; it is sensitive to its parameters and struggles in high dimensions.")
q("feature-scaling", "For which algorithm is feature scaling LEAST important?",
  ["k-nearest neighbours", "Support vector machine", "Decision tree", "k-means"],
  "C", "Trees split on thresholds one feature at a time, so they are invariant to monotonic scaling; distance-based methods are not.")
q("encoding", "What is the usual way to encode a nominal categorical variable with no natural order (e.g. 'card', 'cash', 'voucher') for a linear model?",
  ["Label encoding", "One-hot encoding", "Ordinal encoding", "Min–max scaling"],
  "B", "Integer (label/ordinal) codes imply a false ordering; one-hot avoids that.")

# --- Neural networks ------------------------------------------------------------------
q("activation", "Which activation function is typically used in the output layer for multi-class classification?",
  ["ReLU", "Softmax", "Sigmoid", "Tanh"],
  "B", "Softmax converts logits into a probability distribution summing to 1. Sigmoid suits binary or multi-label outputs.")
q("backprop", "What does backpropagation compute in a neural network?",
  ["Gradients of the loss for each weight, via the chain rule", "The step size used to update each weight during training", "The predicted output for each example in the batch", "The initial random values given to each weight"],
  "A", "Backprop computes gradients; the optimiser then applies them using the learning rate.")
q("learning-rate", "Training loss oscillates wildly and increases. What is the most likely cause?",
  ["The learning rate is too high", "The learning rate is too low", "The batch size is too large", "The network has too few layers"],
  "A", "A large learning rate overshoots minima and can cause divergence.")

# --- Generative AI -------------------------------------------------------------------
q("rag", "What is the main purpose of Retrieval-Augmented Generation (RAG)?",
  ["To update the model's weights with new documents", "To ground responses in documents retrieved at query time", "To compress a large model into a smaller one", "To filter harmful content from model outputs"],
  "B", "RAG retrieves relevant chunks (often via vector search) and supplies them as context, reducing hallucination without retraining. Updating weights is fine-tuning; compression is distillation.")
q("hallucination", "An LLM confidently cites a policy document that does not exist. This is known as:",
  ["Hallucination", "Prompt injection", "Overfitting", "Model drift"],
  "A", "Hallucination is plausible but fabricated output; mitigations include grounding, citation checks and human review.")
q("temperature", "Lowering the 'temperature' parameter when sampling from an LLM generally:",
  ["Makes outputs more varied and creative", "Makes outputs more deterministic", "Shortens the length of the output", "Increases the size of the context window"],
  "B", "Low temperature sharpens the probability distribution over tokens.")

# --- Simulation & optimisation -----------------------------------------------------------
q("monte-carlo", "Monte Carlo simulation is used to:",
  ["Estimate outcome distributions by repeatedly sampling uncertain inputs", "Find the exact optimum of a linear objective under constraints", "Model entities moving through queues as a sequence of events", "Fit a model's parameters by maximising the likelihood of the data"],
  "A", "Running many random scenarios gives a distribution of results and risk estimates.")
q("discrete-event", "Modelling queues at a customer contact centre to test staffing levels is best done with:",
  ["Discrete-event simulation", "Monte Carlo integration", "Linear programming", "System dynamics"],
  "A", "Discrete-event simulation models entities moving through queues and processes over time. System dynamics models aggregate stocks and flows.")
q("linear-programming", "Allocating a fixed budget across sites to maximise total benefit, with linear constraints on staff and cost, is best formulated as:",
  ["Linear programming", "Monte Carlo simulation", "Logistic regression", "Cluster analysis"],
  "A", "LP optimises a linear objective subject to linear constraints; integer programming if decisions are whole numbers.")
q("heuristics", "Why might a genetic algorithm or simulated annealing be used instead of an exact optimisation method?",
  ["They find a proven global optimum more quickly than exact solvers", "The problem is large or non-convex, so a good solution is enough", "They work without needing an objective function to be defined", "They are designed for small problems with linear constraints"],
  "B", "Metaheuristics trade guaranteed optimality for tractability on hard problems.")

# --- Production ML / automation -------------------------------------------------------
q("drift", "A model's input data distribution changes (e.g. new sensor types), though the underlying relationship is unchanged. This is:",
  ["Data drift", "Concept drift", "Label leakage", "Model decay"],
  "A", "Data drift (covariate shift) = change in P(X); concept drift = change in the relationship P(y|X).")
q("drift", "After a policy change, the relationship between customer features and complaint likelihood changes. This is:",
  ["Concept drift", "Data drift", "Sampling bias", "Label noise"],
  "A", "Concept drift means the target mapping itself has changed, so the model needs retraining.")
q("mlops", "Which TWO activities are part of MLOps for a model in production?",
  ["Monitoring prediction quality and data drift", "Versioning models, data and code together", "Retraining manually only when users complain", "Keeping the production model in a notebook"],
  "AB", "MLOps covers versioning, automated deployment, monitoring and planned retraining.")
q("explainability", "Which technique attributes an individual prediction to the contribution of each input feature, based on cooperative game theory?",
  ["SHAP values", "Permutation importance", "Partial dependence plots", "Gini importance"],
  "A", "SHAP uses Shapley values for local explanations. Permutation and Gini importance are global; PDPs show average effects.")
q("rpa", "Robotic Process Automation (RPA) is best described as:",
  ["Software bots that repeat rule-based actions in user interfaces", "Machine learning models that predict which tasks to automate", "Scheduled scripts that move data between databases nightly", "Physical robots that handle items in a warehouse or factory"],
  "A", "RPA automates rule-based clicks and keystrokes; it is brittle when interfaces change.")
