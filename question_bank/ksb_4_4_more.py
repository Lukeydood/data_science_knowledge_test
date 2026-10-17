from ._helpers import make_builder

q, QUESTIONS = make_builder("4.4", "Computing and organisational resource constraints and trade-offs in selecting models, algorithms and tools", start=101)

q("space-complexity", "A deduplication step builds a Python set of every ID seen. How does its memory use grow with n records?",
  ["Linearly, O(n), one entry per distinct ID", "Constant, O(1) regardless of the number of records", "Quadratically, O(n²) because every pair is stored", "Logarithmically, O(log n) because sets are tree-based"],
  "A", "The set holds one entry per distinct ID, so memory grows in proportion to n.")
q("lookup-structure", "Checking whether each of 1 million IDs is in a list of 100,000 approved IDs is slow. What is the best fix?",
  ["Convert the approved list to a set", "Sort the IDs alphabetically first and then loop", "Run the same loop on a computer with more RAM", "Split the list into ten parts and loop over each"],
  "A", "Set membership is O(1) on average versus O(n) for a list, turning hours into seconds.")
q("dtypes", "Which TWO changes typically reduce the memory used by a large pandas DataFrame?",
  ["Downcasting numeric columns, e.g. float64 to float32", "Converting repetitive strings to the category dtype", "Converting every column to the object dtype", "Adding an index on every column of the frame"],
  "AB", "Smaller numeric types and categoricals cut memory substantially; object dtype is the most memory-hungry.")
q("polars-duckdb", "Why might an analyst use DuckDB or Polars instead of pandas for a 20 GB dataset on a laptop?",
  ["They use columnar, multi-threaded and out-of-core execution", "They store all of the data on a remote cloud server for free", "They require the data to be converted into JSON first", "They avoid reading the data from disk altogether"],
  "A", "Both are designed for fast analytical processing and can work with data larger than memory.")
q("parallelism", "A CPU-bound Python loop is split across 8 processes on an 8-core machine but runs only ~5× faster. Why?",
  ["Overheads such as process start-up and data transfer", "Python processes share one core of the CPU between them", "The machine has fewer cores than the operating system reports", "The machine is throttling the processes to save power"],
  "A", "Parallel speed-up is limited by overheads and serial parts of the work (Amdahl's law).")
q("amdahl", "If 20% of a job cannot be parallelised, what is the maximum possible speed-up however many processors are used?",
  ["5×", "20×", "80×", "Unlimited"],
  "A", "Amdahl's law: max speed-up = 1 / serial fraction = 1 / 0.2 = 5.")
q("gpu-vs-cpu", "For which task is a GPU least likely to give a big speed-up over a CPU?",
  ["Row-by-row business logic with many branches", "Training a convolutional neural network on images", "Large dense matrix multiplications", "Running inference on batches of images"],
  "A", "GPUs excel at uniform, highly parallel arithmetic; branching sequential logic suits CPUs.")
q("caching", "Results of an expensive API call that rarely change are stored and reused for 24 hours. The main trade-off is:",
  ["Speed and cost savings against possibly stale data", "Lower security against higher accuracy of the results", "More code complexity against no benefit", "Higher API costs against faster responses"],
  "A", "Caching improves speed and cost but data may be up to a day old.")
q("incremental-processing", "A nightly job reprocesses 10 years of data even though only yesterday's records changed. What is the better design?",
  ["Incremental processing of new or changed data", "Running the full job on a bigger machine", "Running the full job less often, e.g. monthly", "Converting the data to CSV before processing"],
  "A", "Processing only deltas reduces cost and runtime; design for idempotency and occasional full rebuilds.")
q("model-serving-cost", "Which TWO factors usually drive the running cost of a deployed ML model?",
  ["Volume of predictions and the compute needed per prediction", "Whether the endpoint is always on or scales to zero", "The number of features used during the original EDA", "The colour palette used on the monitoring dashboard"],
  "AB", "Serving cost depends on traffic, model size/latency requirements and how infrastructure scales.")
q("llm-vs-classical", "A team needs to classify 50 million short, well-defined records daily with a fixed set of labels and plentiful training data. Which is likely most cost-effective?",
  ["A trained classical or small transformer classifier", "A frontier LLM prompted for every individual record", "Manual classification by a large team of analysts", "A new foundation model trained from scratch in-house"],
  "A", "With lots of labelled data and high volume, a dedicated model is far cheaper and faster than per-call LLM prompting.")
q("latency-accuracy", "An ensemble improves accuracy slightly but triples prediction latency beyond what a real-time app allows. What should usually happen?",
  ["Choose a model that meets the latency requirement", "Deploy the ensemble and ask users to wait longer", "Remove monitoring so that predictions return faster", "Increase the accuracy target to justify the latency"],
  "A", "Hard non-functional requirements constrain model choice; accuracy gains are worthless if the system is unusable.")
q("open-vs-proprietary-llm", "Which TWO are typical reasons to choose an open-weight LLM hosted in-house over a proprietary API?",
  ["Greater control over where data is processed", "Ability to fine-tune and fix the model version", "Lower total effort to run and maintain it", "Higher accuracy than all proprietary models"],
  "AB", "Self-hosting gives control and stability but adds operational burden; it is not automatically more accurate.")
q("procurement", "In UK public sector organisations, which constraint commonly affects adopting a new commercial analytics tool?",
  ["Procurement rules, security assurance and approval timescales", "A legal ban on most commercial software in central government", "A requirement that every tool is written in Python", "A rule that cloud services may only be used at weekends"],
  "A", "Procurement, information assurance and accreditation can take months and must be planned for.")
q("support-skills", "A team is choosing between R and Python for a new production pipeline. Which factor matters most organisationally?",
  ["Which language the team can support and maintain", "Which language has the shorter name to type", "Which language was released first historically", "Which language uses fewer brackets in its syntax"],
  "A", "Supportability, skills, existing codebase and platform support outweigh small technical differences.")
q("data-volume-model", "Which TWO factors should influence whether to use a deep learning model rather than gradient boosting for tabular data?",
  ["Amount of labelled data available", "Need for interpretability", "Number of rows displayed in the report", "Font used in the project documentation"],
  "AB", "For typical tabular problems, boosted trees are strong, cheaper and easier to explain.")
q("sla-tradeoffs", "A model refreshed weekly is good enough for planning, but a stakeholder asks for real-time updates. What should the data scientist do first?",
  ["Clarify the decision need and the cost of real-time", "Build real-time streaming immediately as requested", "Decline the request, as weekly is sufficient for planning", "Switch to daily updates without discussing it further"],
  "A", "Requirements should be driven by decision value; real-time adds significant cost and complexity.")
q("experiment-cost", "Before running a large hyperparameter sweep on cloud GPUs, which step best controls cost?",
  ["Test on a small sample and set budget limits", "Use the largest GPU type to finish quickly", "Run every combination in parallel at once", "Disable logging to reduce storage charges"],
  "A", "Small-scale trials catch bugs cheaply; budgets and early stopping prevent runaway spend.")
q("maintenance-burden", "Which choice usually increases a model's long-term maintenance burden the most?",
  ["Many bespoke features from fragile upstream sources", "Using a well-documented, widely used library", "Automated tests covering the feature pipeline", "A simple model with a small set of stable, well-understood inputs"],
  "A", "Every external dependency and custom feature is something that can break or drift.")
q("accuracy-fairness", "Improving a model's overall accuracy slightly would worsen error rates for a small protected group. How should this be treated?",
  ["As a trade-off needing explicit, documented judgement", "As irrelevant because overall accuracy improved", "As a reason to stop collecting data on that group", "As a purely technical choice for the data scientist alone"],
  "A", "Fairness trade-offs have ethical and legal implications (e.g. the Equality Act) and need stakeholder input.")
q("explainability-cost", "A simple scorecard is slightly less accurate than a black-box model but staff can apply and check it manually. Which TWO benefits does it offer?",
  ["Transparency to the people affected by decisions", "Easier audit and challenge of individual outcomes", "Higher accuracy than the black-box model on future data", "No need for any validation or monitoring"],
  "AB", "Interpretable models support accountability; they still need validation and monitoring.")
q("streaming-cost", "Why might a team choose micro-batching every 5 minutes instead of true event-by-event streaming?",
  ["Simpler and cheaper, and latency is still acceptable", "It gives lower end-to-end latency than event streaming", "It removes the need to handle late data", "It is required by the Data Protection Act"],
  "A", "Micro-batching trades a little latency for simplicity and cost.")
