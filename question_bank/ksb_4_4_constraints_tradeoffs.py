from ._helpers import make_builder

q, QUESTIONS = make_builder("4.4", "Computing and organisational resource constraints and trade-offs in selecting models, algorithms and tools")

q("interpretability", "A model will make decisions that significantly affect individuals and must be explainable to them and to regulators. Which choice is usually most appropriate?",
  ["A deep neural network, explained afterwards with SHAP", "An interpretable model, if its performance is adequate", "The model with the highest validation accuracy", "An ensemble of several models to reduce the variance"],
  "B", "Accountability requirements often justify trading a little accuracy for a model that is transparent by design; post-hoc explanations are approximations.")
q("interpretability", "Which TWO are typical trade-offs when moving from logistic regression to a large gradient-boosted ensemble?",
  ["Potentially higher predictive accuracy", "Reduced interpretability of predictions", "Lower training and inference compute", "Less need for hyperparameter tuning"],
  "AB", "Complex ensembles may be more accurate but are harder to explain, costlier to run and have more hyperparameters.")
q("baseline", "Why is it good practice to build a simple baseline model before a complex one?",
  ["It gives a benchmark to judge if extra complexity is worth it", "It usually outperforms complex models on messy real-world data", "It removes the need to split data into train and test", "It identifies which features to drop from the final model"],
  "A", "If a complex model barely beats the baseline, the extra cost may not be worthwhile.")
q("diminishing-returns", "A new model improves accuracy by 0.3% but needs ten times the compute and a specialist to maintain it. What is the most reasonable response?",
  ["Adopt it, because higher accuracy should take priority", "Weigh the small gain against cost, skills and maintenance", "Reject it, because complex models are not maintainable", "Retrain it on more data until the gain reaches 1%"],
  "B", "Model selection balances performance with organisational and computing costs; neither automatic adoption nor rejection is justified.")
q("big-o", "An algorithm compares every record with every other record. If the dataset grows from 10,000 to 100,000 records, roughly how much longer will it take?",
  ["10 times", "100 times", "20 times", "1,000 times"],
  "B", "Pairwise comparison is O(n²): 10× the data → 100× the work.")
q("big-o", "Which time complexity scales best as data grows very large?",
  ["O(n²)", "O(n log n)", "O(2ⁿ)", "O(n³)"],
  "B", "O(n log n) grows far more slowly than polynomial or exponential complexity.")
q("memory", "A 60 GB CSV must be analysed on a laptop with 16 GB RAM. Which TWO approaches are appropriate?",
  ["Process it in chunks or with an out-of-core tool like Dask", "Convert to Parquet and read only the columns needed", "Increase the swap file and load it all with pandas", "Read it with a larger pandas dtype for each column"],
  "AB", "Chunking, lazy evaluation and column pruning reduce memory needs; swapping makes a full load extremely slow, and larger dtypes increase memory.")
q("gpu", "Why are GPUs commonly used for training deep learning models?",
  ["They run many parallel matrix operations efficiently", "They have more memory than a typical server's RAM", "They are cheaper per hour than CPU instances", "They run single-threaded code at a higher clock speed"],
  "A", "Deep learning is dominated by large matrix multiplications that parallelise well on GPUs.")
q("latency", "A model must return predictions within 50 ms inside a web application. Which consideration matters most?",
  ["Training time", "Inference latency", "Training data volume", "Number of features"],
  "B", "Real-time use cases constrain inference speed, which may favour a smaller or optimised model; training happens offline.")
q("compression", "Which TWO techniques reduce the size and inference cost of a neural network?",
  ["Quantisation, e.g. 32-bit floats to 8-bit integers", "Knowledge distillation into a smaller student model", "Ensembling several copies of the model together", "Fine-tuning the model on more domain-specific data"],
  "AB", "Quantisation, pruning and distillation shrink models with modest accuracy loss; ensembling increases cost.")
q("batch-vs-realtime-scoring", "Predictions are needed once per day for a planning report. Which deployment approach is usually most cost-effective?",
  ["A continuously running scoring API", "Scheduled batch scoring", "Streaming scoring on each new record", "Deploying the model to edge devices"],
  "B", "Batch scoring avoids the cost and complexity of low-latency infrastructure when it isn't needed.")
q("small-data", "With only 300 labelled examples of tabular data, why might a deep neural network be a poor choice?",
  ["It is likely to overfit; simpler models often do as well", "It takes too long to train on such a small dataset", "It needs images or text rather than tabular inputs", "It gives poorly calibrated probabilities on tabular data"],
  "A", "Deep models are data-hungry; regularised regression or tree ensembles usually generalise better on small tabular data.")
q("llm-cost", "A team uses a large LLM API to classify millions of short texts into five categories. Which TWO options could reduce cost while maintaining acceptable quality?",
  ["Use a smaller model or fine-tuned classifier, checked on a labelled sample", "Batch requests and cache results for repeated inputs", "Add detailed worked examples to every prompt to improve accuracy", "Ask the model to explain its reasoning before giving each label"],
  "AB", "Costs scale with tokens and calls; right-size the model and avoid redundant calls. Longer prompts and reasoning add tokens.")
q("rate-limits", "An external API allows 100 requests per minute. A pipeline needs 50,000 calls. What should the design include?",
  ["Throttling with back-off and retry, spread over time", "Parallel workers so all calls finish within a minute", "A second API key to double the permitted rate", "A long timeout so slow requests are not abandoned"],
  "A", "Respecting rate limits prevents throttling and blocking; exponential back-off handles transient 429 errors. Extra keys to evade limits usually breach terms.")
q("build-vs-buy", "Which TWO factors are most relevant when deciding whether to build a tool in-house or buy a commercial product?",
  ["Total cost of ownership, including support and maintenance", "Whether the team has the skills to build and maintain it", "Whether the vendor's product is written in Python", "How many other public bodies have built their own"],
  "AB", "Build vs buy weighs cost, skills, time to value, fit and lock-in.")
q("open-source", "Which is a common risk of adopting an open-source library for a production pipeline?",
  ["It may be poorly maintained or have an unsuitable licence", "Its licence restricts it to on-premise deployment only", "It needs a commercial support contract to be used in government", "It requires a per-user commercial licence fee"],
  "A", "Check maintenance activity, licence terms (e.g. GPL vs MIT) and security advisories.")
q("skills", "A complex model is built by a contractor who then leaves; nobody in the team understands it. Which constraint was overlooked?",
  ["Team skills and maintainability", "Compute and storage capacity", "Data volume and velocity", "Licensing of the training data"],
  "A", "Models must be supportable by the people who will own them.")
q("prototype-vs-production", "Which TWO are typically needed when moving a prototype notebook model into production?",
  ["Automated tests, logging and monitoring", "Packaged, version-controlled code", "A larger model to absorb new data", "A manual run book for each daily run"],
  "AB", "Production systems need reliability, reproducibility and observability; manual daily runs are what productionising removes.")
q("approximate-algorithms", "Approximate nearest neighbour (ANN) search is often used in vector databases because:",
  ["It returns the exact nearest vectors with less memory", "It trades a little accuracy for large gains in speed", "It removes the need to compute embeddings at all", "It reduces every vector to a single scalar value"],
  "B", "Exact search over millions of vectors is slow; ANN indexes such as HNSW are much faster with slightly imperfect recall.")
q("sampling-prototype", "Why might an analyst develop code on a random sample of a very large dataset first?",
  ["To iterate quickly and cheaply before running at full scale", "To produce more accurate estimates than the full dataset gives", "To avoid needing to validate results on the full data", "To reduce bias that exists in the full dataset"],
  "A", "Rapid iteration on samples saves time and compute; results should then be validated on full data.")
q("vectorisation", "Why is vectorised NumPy/pandas code usually faster than Python loops over rows?",
  ["Operations run in optimised compiled code over whole arrays", "Operations run on the GPU automatically when one is available", "Operations use lower-precision numbers to save time", "Operations are cached so repeated runs are skipped"],
  "A", "Vectorisation moves work out of the Python interpreter into optimised C.")
q("security-constraints", "Highly sensitive data cannot leave the organisation's environment. Which TWO options respect this constraint for an NLP task?",
  ["Use a model hosted in the organisation's approved tenancy", "Minimise or anonymise the data under approved controls", "Use a public chatbot with chat history switched off", "Process the data on a personal device outside the network"],
  "AB", "Information governance can restrict tool choice; deploy within approved boundaries. Turning off history doesn't keep data inside the organisation.")
q("sustainability", "Which TWO actions reduce the environmental (energy/carbon) impact of machine learning work?",
  ["Choosing smaller models that meet the requirement", "Avoiding unnecessary retraining and large tuning sweeps", "Training in several regions at once for redundancy", "Keeping GPU instances warm between experiments"],
  "AB", "Compute consumption drives energy use; right-sizing and efficiency reduce it.")
q("edge-constraints", "A model will run on a battery-powered field device with limited memory. Which consideration is most important?",
  ["Model size and power use", "Training dataset size", "Cloud storage tier", "Number of output classes"],
  "A", "Edge deployment favours compact, efficient models.")
q("tech-debt-ml", "In ML systems, 'technical debt' commonly arises from:",
  ["Glue code and undocumented data dependencies", "Pinning dependency versions in a lock file", "Running automated tests in a CI pipeline", "Recording assumptions in a model card"],
  "A", "Shortcuts taken to ship quickly accumulate maintenance costs later; the other options reduce debt.")
