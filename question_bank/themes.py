"""Broad-theme Google searches for revision.

Each question's concept is mapped to a broad theme, written as a search phrase
that leads to general reading on the topic behind the question (e.g. the
base-rate question maps to "cognitive biases in decision making"). Shown to
the candidate after marking, never before.

Every concept in the bank must appear exactly once in its KSB's mapping;
`question_bank.validate` enforces this.
"""

THEMES = {
    "3.1": {
        "cloud computing service models IaaS PaaS SaaS explained": [
            "cloud-models", "serverless", "shared-responsibility", "managed-identity", "cold-start"],
        "on-premise vs cloud computing pros and cons": [
            "onprem-vs-cloud", "capex-opex", "hybrid-cloud", "vendor-lock-in", "data-sovereignty",
            "on-prem-scenarios", "elasticity", "spot-instances", "cost-management", "egress"],
        "batch vs stream data processing and ETL pipelines": [
            "batch-vs-stream", "etl-elt", "orchestration", "dag", "idempotency", "latency-throughput"],
        "data lake vs data warehouse vs lakehouse architecture": [
            "data-lake", "schema-on-read", "lakehouse", "time-travel", "data-virtualisation",
            "compute-storage", "small-files", "partitioning"],
        "cloud storage types and tiers explained": [
            "object-storage", "storage-types", "storage-tiers", "nas-san", "data-lifecycle"],
        "distributed data processing Hadoop and Spark explained": [
            "hdfs", "spark", "spark-lazy", "spark-shuffle", "mapreduce"],
        "containers Docker and Kubernetes explained": ["containers", "kubernetes", "iac", "edge-computing"],
        "backup disaster recovery and high availability in the cloud": [
            "rpo-rto", "backup-321", "replication", "availability-zones", "sla-maths", "dr-strategies"],
        "cloud data security best practices": ["encryption", "least-privilege"],
    },
    "3.2": {
        "relational database fundamentals ACID keys and normalisation": [
            "acid", "normalisation", "keys", "composite-key", "indexes", "locking", "isolation-anomaly"],
        "SQL query fundamentals tutorial": [
            "sql-where-having", "sql-joins", "sql-order", "sql-count", "sql-null", "window-functions",
            "union", "cte", "materialised-view"],
        "data warehousing and dimensional modelling explained": [
            "star-schema", "denormalisation", "scd", "data-mart", "kimball-inmon", "surrogate-key", "grain",
            "additive-measures", "conformed-dimension", "star-vs-3nf"],
        "OLTP vs OLAP and analytical database architecture": [
            "oltp-olap", "olap-ops", "columnar", "mpp", "molap-rolap", "htap", "in-memory"],
        "types of NoSQL databases and when to use them": [
            "nosql-types", "nosql-pros-cons", "document-modelling", "key-design", "polyglot", "search-engine",
            "vector-db", "time-series-db"],
        "distributed database scaling and consistency CAP theorem": [
            "scaling", "cap", "base", "sharding", "replication-lag"],
        "real-time data streaming architecture explained": [
            "kafka", "cdc", "lambda-kappa", "windowing", "event-time", "delivery-semantics", "stream-db"],
    },
    "3.3": {
        "correlation vs causation and causal inference": [
            "correlation-causation", "confounding", "reverse-causation", "rct", "quasi-experiment",
            "counterfactual", "hawthorne"],
        "hierarchy of evidence and evaluating evidence quality": [
            "evidence-hierarchy", "evidence-strength", "triangulation"],
        "cognitive biases in decision making": [
            "confirmation-bias", "anchoring", "availability", "base-rate", "sunk-cost", "optimism-bias",
            "groupthink", "framing"],
        "statistical biases and paradoxes in data analysis": [
            "survivorship-bias", "selection-bias", "simpsons-paradox", "regression-to-mean", "ecological-fallacy",
            "p-hacking"],
        "statistical vs practical significance and communicating uncertainty": [
            "practical-significance", "communicating-uncertainty", "expected-value", "decision-tree-analysis",
            "sensitivity-analysis", "scenario-analysis"],
        "types of data analytics descriptive diagnostic predictive prescriptive": ["analytics-types", "data-maturity"],
        "data quality dimensions explained": ["data-quality"],
        "UK government analysis guidance Aqua Book Green Book Magenta Book": [
            "aqua-book", "green-book", "magenta-book", "qa-roles", "proportionate-qa", "model-risk",
            "statistics-code"],
        "UK GDPR data protection principles": ["gdpr-principles", "dpia", "five-safes"],
        "data ethics and algorithmic fairness in the public sector": [
            "data-ethics", "algorithmic-transparency", "bias-in-models", "equality-duty"],
        "KPIs and performance metrics best practice": ["goodharts-law", "leading-lagging", "smart", "vanity-metrics"],
        "data visualisation best practice for decision makers": [
            "chart-choice", "chart-integrity", "dashboard-design", "storytelling", "colour-accessibility"],
    },
    "4.1": {
        "descriptive statistics measures of centre and spread": [
            "central-tendency", "spread", "iqr-outliers", "z-score", "variance-calc", "sample-variance",
            "percentiles", "kurtosis"],
        "probability rules and Bayes theorem": [
            "independence", "bayes", "conditional-probability", "mutually-exclusive", "complement", "combinations",
            "expected-value-dice"],
        "common probability distributions in statistics": [
            "distributions", "normal-rule", "clt", "law-large-numbers", "standard-error"],
        "hypothesis testing p-values and confidence intervals": [
            "p-value", "errors", "confidence-interval", "multiple-testing", "one-two-tailed", "effect-size",
            "sample-size", "bootstrap"],
        "choosing the right statistical test": [
            "test-choice", "paired-test", "anova-assumptions", "normality-test", "qq-plot", "correlation"],
        "linear and logistic regression explained": [
            "regression-assumptions", "r-squared", "multicollinearity", "logistic", "log-transform",
            "residual-plot", "interaction", "adjusted-r2", "aic", "poisson-regression", "overdispersion"],
        "linear algebra and calculus for data science": [
            "matrix-dims", "pca-eigen", "gradient-descent", "dot-product", "matrix-inverse", "derivative",
            "logarithms"],
        "time series analysis and forecasting basics": [
            "time-series", "stationarity", "moving-average", "exp-smoothing", "acf"],
        "survival analysis explained": ["survival"],
    },
    "4.2": {
        "types of machine learning supervised unsupervised reinforcement": ["learning-types", "task-type"],
        "overfitting bias variance tradeoff and regularisation": [
            "overfitting", "bias-variance", "regularisation", "pruning", "dropout"],
        "model validation and hyperparameter tuning": [
            "cross-validation", "data-leakage", "hyperparameters", "tuning", "stratified-split", "validation-set",
            "group-leakage"],
        "classification and regression evaluation metrics": [
            "precision-recall", "imbalance", "roc-auc", "regression-metrics", "f1", "specificity",
            "confusion-matrix", "threshold", "pr-vs-roc", "calibration"],
        "supervised machine learning algorithms explained": [
            "random-forest", "boosting", "svm", "knn", "naive-bayes", "decision-tree-split"],
        "clustering and dimensionality reduction": [
            "kmeans", "dbscan", "hierarchical-clustering", "silhouette", "dim-reduction", "tsne-umap"],
        "feature engineering and data preprocessing for machine learning": ["feature-scaling", "encoding"],
        "neural networks and deep learning fundamentals": [
            "activation", "backprop", "learning-rate", "autoencoder", "batch-epoch", "vanishing-gradient",
            "rnn-lstm", "transfer-learning"],
        "large language models and retrieval augmented generation": [
            "rag", "hallucination", "temperature", "prompting", "llm-eval", "prompt-injection", "embeddings-rag"],
        "simulation and optimisation methods in operational research": [
            "monte-carlo", "discrete-event", "linear-programming", "heuristics", "optimisation-terms",
            "integer-programming", "local-optimum", "agent-based"],
        "MLOps and machine learning in production": ["drift", "mlops", "explainability"],
        "time series forecasting with machine learning": ["time-series-ml", "prophet-arima", "forecast-metrics"],
        "intelligent automation and robotic process automation": ["rpa", "automation-llm"],
    },
    "4.3": {
        "natural language processing text preprocessing": [
            "tokenisation", "stop-words", "stem-lemma", "pos-tagging", "regex", "normalisation-text", "subword",
            "language-detection"],
        "text representation bag of words TF-IDF and embeddings": [
            "bag-of-words", "tf-idf", "n-grams", "embeddings", "cosine", "contextual-embeddings",
            "sentence-embeddings"],
        "transformers and large language models explained": [
            "transformers", "bert-gpt", "context-window", "perplexity", "chunking"],
        "common NLP tasks and applications": [
            "ner", "topic-modelling", "sentiment", "summarisation", "pii-redaction", "speech", "nlp-metrics"],
        "text classification with machine learning": [
            "transfer-learning-nlp", "zero-shot", "active-learning", "label-quality", "multi-label",
            "text-classification-baseline"],
        "computer vision and convolutional neural networks basics": [
            "image-repr", "cnn", "pooling", "receptive-field", "normalising-images", "class-activation"],
        "computer vision tasks classification detection segmentation": [
            "cv-tasks", "iou", "yolo", "map-metric", "nms", "video", "ocr", "multimodal"],
        "training computer vision models with limited data": [
            "augmentation", "transfer-learning-cv", "labelling-tools", "domain-shift", "edge-cv"],
        "remote sensing and satellite imagery analysis": ["ndvi", "change-detection", "cloud-cover", "sar"],
        "ethics of computer vision and generative AI": ["cv-ethics", "generative-images"],
    },
    "4.4": {
        "choosing machine learning models trade-offs accuracy vs interpretability": [
            "interpretability", "baseline", "diminishing-returns", "small-data", "data-volume-model",
            "latency-accuracy", "accuracy-fairness", "explainability-cost"],
        "algorithm time and space complexity Big O": [
            "big-o", "space-complexity", "lookup-structure", "approximate-algorithms"],
        "working with large datasets in Python memory and performance": [
            "memory", "dtypes", "polars-duckdb", "vectorisation", "sampling-prototype", "parallelism", "amdahl",
            "caching", "incremental-processing"],
        "CPU vs GPU for machine learning and model compression": ["gpu", "gpu-vs-cpu", "compression", "edge-constraints"],
        "deploying machine learning models cost and latency": [
            "latency", "batch-vs-realtime-scoring", "model-serving-cost", "streaming-cost", "sla-tradeoffs",
            "prototype-vs-production"],
        "cost of using large language models vs traditional machine learning": [
            "llm-cost", "llm-vs-classical", "open-vs-proprietary-llm", "rate-limits", "experiment-cost"],
        "build vs buy software decisions and open source risks": ["build-vs-buy", "open-source", "procurement"],
        "organisational constraints in data science projects skills and maintenance": [
            "skills", "support-skills", "tech-debt-ml", "maintenance-burden"],
        "data security and sustainability considerations in AI": ["security-constraints", "sustainability"],
    },
    "4.5": {
        "Git version control basics tutorial": [
            "git-basics", "git-staging", "git-status", "git-diff", "git-stash", "revert-reset", "gitignore",
            "large-files", "commit-messages", "small-commits"],
        "Git branching strategies pull requests and code review": [
            "branching", "pull-requests", "merge-conflict", "rebase-merge", "branch-protection", "code-review-focus",
            "pair-programming"],
        "software testing types unit integration regression": [
            "test-types", "uat", "tdd", "mocking", "coverage", "edge-cases", "property-testing", "snapshot-testing"],
        "pytest tutorial fixtures and parametrize": ["assertions", "fixtures", "parametrise"],
        "testing data pipelines and data validation": ["data-testing"],
        "CI/CD for data science projects": ["ci-cd", "github-actions", "pre-commit", "model-versioning"],
        "reproducible data science environments and packaging": [
            "reproducibility-env", "docker", "rap", "notebooks", "packaging", "dependency-pinning", "semver"],
        "Python coding best practices clean code": [
            "pep8", "linting", "dry", "docstrings", "exceptions", "logging", "magic-numbers", "type-checking",
            "functions-design", "config", "readme", "licence"],
        "secure coding practices for data scientists": ["secrets", "security-deps", "sql-injection"],
        "agile delivery Scrum and Kanban for data teams": ["agile", "definition-of-done", "kanban-scrum"],
    },
    "5.1": {
        "primary vs secondary data sources": ["primary-secondary", "survey-data", "crowdsourced", "files"],
        "REST APIs and HTTP basics for data scientists": [
            "rest-api", "http-status", "pagination", "api-auth", "query-params", "http-post", "status-5xx",
            "graphql", "soap", "webhooks"],
        "web scraping ethics and legality": ["web-scraping"],
        "UK open government data sources": [
            "open-data", "hydrology-api", "ons-data", "official-stats", "data-revisions", "geospatial-sources",
            "weather-data", "foi"],
        "administrative and operational data for analysis": [
            "operational-systems", "admin-data", "database-connection", "odbc-jdbc", "logs"],
        "using social media and news data for research": [
            "social-media", "news-data", "social-media-api", "sampling-social", "news-api"],
        "IoT sensor data quality issues": ["sensor-data"],
        "data protection and anonymisation of personal data": ["anonymisation", "special-category", "data-sharing", "synthetic-data"],
        "data governance metadata and data lineage": [
            "provenance", "metadata", "fair", "data-catalogue", "information-asset-owner", "master-data",
            "reference-data", "identifiers"],
        "assessing reliability of data sources": ["source-reliability", "data-quality-source"],
    },
    "5.2": {
        "structured semi-structured and unstructured data": [
            "structure-types", "unstructured-processing", "audio-video", "pdf-extraction"],
        "data file formats CSV JSON Parquet Avro compared": [
            "csv-pitfalls", "parquet", "avro", "json-xml", "json-types", "jsonl", "yaml", "xml-parsing", "arrow",
            "delta-iceberg", "binary-serialisation", "compression", "fixed-width", "pickle", "api-formats"],
        "common data cleaning problems encodings dates and Excel": [
            "encoding", "encoding-bom", "delimiter", "excel-pitfalls", "excel-format", "dates", "time-zones",
            "unix-time", "leading-zeros", "data-types"],
        "geospatial data formats and coordinate reference systems": [
            "spatial-formats", "raster-vector", "netcdf", "geopackage", "crs", "wkt"],
        "tidy data and reshaping data structures": ["tidy-data", "long-wide", "nested-json", "nested-structure", "graph-structure"],
        "data delivery methods APIs files and streaming": [
            "delivery", "message-queue", "pub-sub", "sftp", "api-vs-file", "data-share", "bulk-vs-incremental"],
        "schema evolution data contracts and API versioning": ["schema-evolution", "data-contract", "api-versioning"],
    },
    "5.3": {
        "handling missing data in statistics": [
            "missingness", "imputation", "placeholder-values", "missing-indicator", "multiple-imputation",
            "listwise-deletion", "forward-fill"],
        "outlier and anomaly detection methods": [
            "outliers", "anomaly-detection", "outlier-robust", "winsorising", "mad", "contextual-anomaly",
            "collective-anomaly"],
        "common distributions in real-world data skewed heavy-tailed": [
            "skew", "power-law", "pareto", "bimodal", "benford", "zero-inflation", "heaping", "long-tail-categories"],
        "time series patterns trend seasonality and stationarity": [
            "seasonality", "trend-cycle", "autocorrelation", "trend-detection", "seasonal-adjustment",
            "calendar-effects", "non-stationary", "random-walk", "correlation-time"],
        "spatial data patterns and the modifiable areal unit problem": ["spatial-autocorrelation", "aggregation", "aggregation-bias"],
        "data drift and changes in data collection over time": [
            "drift-real-world", "structural-break", "data-collection-change", "feedback-loop"],
        "data cleaning duplicates and inconsistent values": [
            "duplicates", "inconsistent-categories", "duplicates-time", "free-text-variation", "unit-inconsistency"],
        "regression problems with real-world data heteroscedasticity multicollinearity": [
            "heteroscedasticity", "multicollinearity-real", "hierarchical", "class-imbalance"],
        "measurement error censoring and detection limits": [
            "censoring", "measurement-error", "rounding-precision", "detection-limit"],
        "sampling and survivorship bias in real-world data": ["survivorship-data", "sample-selection", "survivorship-model"],
    },
    "GEN": {
        "Python fundamentals for data science": [
            "py-mutable", "py-default-arg", "py-comprehension", "py-dict-get", "py-generator", "py-is-eq",
            "py-float", "py-venv", "py-with", "py-fstring", "py-zero-index", "py-negative-index"],
        "pandas and NumPy tutorial for data analysis": [
            "pd-loc-iloc", "pd-groupby", "pd-merge", "pd-merge-dupes", "pd-settingwithcopy", "pd-isna", "pd-apply",
            "pd-pivot", "pd-datetime", "pd-resample", "np-broadcast", "np-axis"],
        "SQL for data analysis tutorial": [
            "sql-distinct", "sql-like", "sql-case", "sql-coalesce", "sql-row-number", "sql-explain", "sql-self-join"],
        "data science tools and workflow": ["jupyter-restart", "cli-basics", "regex-basics", "r-vs-python", "bi-tools"],
        "data science project lifecycle CRISP-DM": [
            "crisp-dm", "crisp-dm-order", "eda", "problem-framing", "mvp", "data-dictionary", "model-card"],
        "experimental design and A/B testing": ["ab-test", "ab-peeking", "power-analysis", "control-group", "blinding"],
        "causal inference methods with observational data": ["observational", "dag-causal"],
        "sampling methods in statistics": ["sampling-methods", "cluster-sampling", "bias-sampling"],
        "machine learning fundamentals and feature engineering": [
            "ols", "dummy-trap", "standardise", "feature-engineering", "target-leakage", "ensembles-stacking",
            "curse-dimensionality", "learning-curves", "early-stopping", "association-rules", "recommender",
            "spatial-interp"],
        "data visualisation best practice": [
            "viz-distribution", "viz-relationship", "box-plot", "dual-axis", "small-multiples",
            "accessibility-charts", "plain-english"],
        "responsible AI fairness and privacy": [
            "fairness-metrics", "proxy-discrimination", "human-in-loop", "re-identification", "differential-privacy",
            "environmental-cost"],
    },
}


def _index():
    idx = {}
    for ksb, themes in THEMES.items():
        for theme, concepts in themes.items():
            for c in concepts:
                key = f"{ksb}:{c}"
                if key in idx:
                    raise ValueError(f"Concept {key} is mapped to more than one theme")
                idx[key] = theme
    return idx


CONCEPT_THEME = _index()


def theme_for(question: dict):
    return CONCEPT_THEME.get(question["concept"])
