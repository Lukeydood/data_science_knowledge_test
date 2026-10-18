"""Coverage extension for every assessed KSB.

Two kinds of question:
- gap-fillers (ids x.y-2nn): topics named or implied by the KSB wording that the
  original modules did not cover;
- broad scenarios (ids x.y-3nn): applied questions that draw on several KSBs at
  once, set in a range of industries.
"""
from ._helpers import make_builder

TITLES = {
    "3.1": "Data processing and storage, including on-premise and cloud technologies",
    "3.2": "Database systems: relational, data warehousing & OLAP, NoSQL and real-time; pros and cons",
    "3.3": "Data-driven decision making and the good use of evidence and analytics",
    "4.1": "Statistical and mathematical models and methods",
    "4.2": "Advanced and predictive analytics, machine learning and AI, simulation, optimisation and automation",
    "4.3": "Applications such as computer vision and natural language processing",
    "4.4": "Computing and organisational resource constraints and trade-offs in selecting models, algorithms and tools",
    "4.5": "Development standards, including programming practice, testing and source control",
    "5.1": "Sources of data: files, operational systems, databases, web services, open/government data, news and social media",
    "5.2": "Data formats, structures and data delivery methods, including unstructured data",
    "5.3": "Common patterns in real-world data",
}
QUESTIONS = []
_gap = {k: make_builder(k, t, start=201) for k, t in TITLES.items()}
_broad = {k: make_builder(k, t, start=301) for k, t in TITLES.items()}


def g(ksb, *args):
    _gap[ksb][0](*args)


def b(ksb, *args):
    _broad[ksb][0](*args)


# =========================== 3.1 =========================================
g("3.1", "big-data-vs", "In the 'Vs' often used to describe big data, what does velocity refer to?",
  ["The speed data arrives and must be processed", "The total amount of data being stored", "The range of formats and sources of data", "The trustworthiness and accuracy of data"],
  "A", "Volume = amount, velocity = speed, variety = range of formats, veracity = trustworthiness, value = usefulness.")
g("3.1", "virtualisation", "What does a hypervisor do?",
  ["Runs several virtual machines on one physical server", "Schedules containers across a cluster of nodes", "Balances network traffic between web servers", "Replicates storage blocks between data centres"],
  "A", "Hypervisors (e.g. Hyper-V, VMware ESXi, KVM) virtualise hardware so one server can host many VMs. Container scheduling is Kubernetes' job.")
g("3.1", "raid-vs-backup", "RAID 1 (disk mirroring) on a database server mainly protects against:",
  ["Data loss when a single disk fails", "Accidental deletion of rows by a user", "Ransomware encrypting the database files", "A whole data centre losing power"],
  "A", "RAID copies every change to the mirror instantly, so deletions and ransomware are copied too. It improves availability but is not a backup.")
g("3.1", "medallion", "In a 'medallion' lakehouse design, what is usually held in the bronze layer?",
  ["Raw data as ingested from source systems", "Cleaned, conformed data ready for joining", "Business-level aggregates for reporting", "Machine learning features for serving"],
  "A", "Bronze = raw, silver = cleaned and conformed, gold = business-ready aggregates.")
g("3.1", "data-mesh", "Data mesh is an approach in which:",
  ["Domain teams own and publish their data as products", "All data is copied into one central enterprise warehouse", "Every table is replicated to each regional cloud", "One central team builds every pipeline for everyone"],
  "A", "Data mesh decentralises ownership to domains, with shared standards and self-serve platforms, instead of one central data team.")
g("3.1", "multi-cloud", "Running workloads across two or more public cloud providers is called:",
  ["Multi-cloud", "Hybrid cloud", "Private cloud", "Community cloud"],
  "A", "Hybrid cloud combines private/on-premise infrastructure with public cloud; multi-cloud uses several public providers.")
g("3.1", "cdn", "A content delivery network (CDN) improves performance mainly by:",
  ["Serving cached content from locations near users", "Compressing databases to reduce storage costs", "Encrypting traffic between internal services", "Running analytics queries in parallel"],
  "A", "CDNs cache static content at edge locations worldwide to cut latency and load on the origin server.")

b("3.1", "broad-scaling", "A start-up's analytics run on one office server that is now too slow, and demand is very uneven through the year. Which TWO changes best address this?",
  ["Move to cloud services that scale with demand", "Separate storage from compute so each can grow", "Buy a larger server sized for the busiest week", "Run all analysis overnight to avoid the peaks"],
  "AB", "Elastic cloud resources and separate storage and compute match capacity to uneven demand; a server sized for the peak sits idle most of the year.")
b("3.1", "broad-health-cloud", "A hospital trust wants to analyse patient records using cloud services. Which TWO issues must be settled first?",
  ["Where the data will be stored and under which laws", "Who is responsible for securing the data and access", "Which colour scheme the dashboards will use", "How many CPUs the provider has in total"],
  "AB", "Data residency and the shared responsibility model come first for sensitive data; health data is special category data under UK GDPR.")

# =========================== 3.2 =========================================
g("3.2", "erd-cardinality", "In an entity-relationship model, a customer can place many orders and each order belongs to one customer. This is a:",
  ["One-to-many relationship", "One-to-one relationship", "Many-to-many relationship", "Recursive relationship"],
  "A", "The foreign key (customer_id) goes on the 'many' side, in the orders table.")
g("3.2", "junction-table", "Students can enrol on many courses and each course has many students. How is this usually modelled in a relational database?",
  ["With a linking table of student–course pairs", "With a list of courses held in one student column", "With a separate student table for every course", "With repeated columns course_1, course_2 and so on"],
  "A", "Many-to-many relationships are resolved with a junction (bridge) table holding both foreign keys.")
g("3.2", "ddl-dml", "Which of these is a Data Definition Language (DDL) statement?",
  ["CREATE TABLE", "INSERT INTO", "UPDATE … SET", "SELECT … FROM"],
  "A", "DDL defines structure (CREATE, ALTER, DROP); DML changes or reads data (INSERT, UPDATE, DELETE, SELECT).")
g("3.2", "transactions-sql", "Within a database transaction, which command undoes all changes made since the transaction began?",
  ["ROLLBACK", "COMMIT", "TRUNCATE", "CHECKPOINT"],
  "A", "COMMIT makes changes permanent; ROLLBACK discards them, supporting atomicity.")
g("3.2", "views", "What is a standard (non-materialised) SQL view?",
  ["A saved query that behaves like a virtual table", "A physical copy of a table refreshed each night", "An index that speeds up queries on a table", "A backup of the table at a point in time"],
  "A", "A view stores the query, not the data, and runs it when used. It can simplify queries and restrict which columns users see.")
g("3.2", "data-vault", "Data Vault modelling organises a warehouse into:",
  ["Hubs, links and satellites", "Facts, dimensions and marts", "Bronze, silver and gold layers", "Nodes, edges and properties"],
  "A", "Hubs hold business keys, links hold relationships, satellites hold descriptive history – designed for auditability and change.")
g("3.2", "stored-procedure", "A stored procedure is:",
  ["SQL code saved in the database and run on request", "A log of every query executed on the database", "A schedule that copies tables to a warehouse nightly", "A rule that rejects rows breaking a foreign key"],
  "A", "Stored procedures keep logic close to the data; constraints enforce rules and query logs record history.")

b("3.2", "broad-shop-design", "An online shop needs fast order processing and monthly sales trend analysis. Which design fits best?",
  ["An OLTP database for orders feeding a separate warehouse", "One shared spreadsheet updated by hand by both teams", "A graph database used for both orders and trend reports", "A key-value cache as the only store for all the data"],
  "A", "Separating transactional and analytical workloads protects order processing and gives analysts a model built for aggregation.")
b("3.2", "broad-ride-hailing", "A ride-hailing app must match drivers and riders within seconds and keep a full history for analysis. Which TWO components are most appropriate?",
  ["An event-streaming platform for live trip events", "A data warehouse or lake for historical analysis", "A nightly CSV export as the only data feed", "A single relational table holding all history"],
  "AB", "Real-time matching needs streaming; long-term analysis needs a store designed for history – a Lambda/Kappa-style combination.")

# =========================== 3.3 =========================================
g("3.3", "discounting", "Why are future costs and benefits discounted in a cost-benefit analysis?",
  ["People value money and benefits now more than later", "Future figures are less precise than current ones", "Discounting removes the effect of inflation on prices", "Discounting makes long projects look more attractive"],
  "A", "Discounting reflects time preference, so net present value compares options fairly. Inflation is handled separately using real prices.")
g("3.3", "five-whys", "Repeatedly asking 'why?' to trace a problem back to its underlying cause is the:",
  ["Five whys technique", "Delphi method", "SWOT analysis", "Pareto analysis"],
  "A", "Root-cause techniques (five whys, fishbone diagrams) help diagnostic analytics avoid treating symptoms.")
g("3.3", "hippo", "A decision is made because the most senior person in the room prefers it, despite contrary data. This is often called:",
  ["The HiPPO effect", "The Hawthorne effect", "The halo effect", "The Pygmalion effect"],
  "A", "HiPPO = highest paid person's opinion. Data-driven cultures make evidence, not seniority, the deciding factor.")
g("3.3", "framing-the-question", "Before starting an analysis to support a decision, which TWO steps matter most?",
  ["Agree the decision the analysis will inform", "Agree how success will be measured", "Choose the most advanced model available", "Design the final dashboard layout"],
  "AB", "Clear questions and success measures keep the analysis decision-relevant; tools and presentation come later.")
g("3.3", "risk-scoring", "A risk register usually scores each risk by which TWO factors?",
  ["Likelihood", "Impact", "Data volume", "Model accuracy"],
  "AB", "Risk = likelihood × impact, often shown on a risk matrix to prioritise mitigations.")
g("3.3", "proxy-metrics", "A team uses 'time spent on site' as a proxy for customer satisfaction. What is the main risk?",
  ["The proxy may not move with the real outcome", "Proxies are too expensive to measure well", "Time data is too noisy to collect at all", "Proxies are banned from formal KPIs"],
  "A", "Long visits may mean frustration, not satisfaction. Validate proxies against the outcome they stand for.")

b("3.3", "broad-board-choice", "A board is choosing between two marketing strategies using an analyst's model. Which TWO actions make the decision better informed?",
  ["Show the range of likely outcomes, not just one number", "Test how sensitive the result is to key assumptions", "Present only the option the analyst prefers", "Remove the caveats so the message is clearer"],
  "AB", "Communicating uncertainty and sensitivity lets decision-makers judge risk; hiding options or caveats undermines good evidence use.")
b("3.3", "broad-redesign", "A retailer's dashboard shows sales rose after a website redesign. Before crediting the redesign, which TWO things should be checked?",
  ["Whether other changes, such as a promotion, happened at the same time", "Whether the same period last year also showed a rise", "Whether the dashboard uses the company's brand colours", "Whether the redesign team prefers the new site"],
  "AB", "Confounders and seasonality are the usual alternative explanations; an A/B test would give stronger evidence.")

# =========================== 4.1 =========================================
g("4.1", "mle", "Maximum likelihood estimation chooses parameter values that:",
  ["Make the observed data most probable", "Minimise the number of parameters used", "Give the widest confidence intervals", "Match the prior belief exactly"],
  "A", "MLE maximises the likelihood of the data given the parameters. For a normal model it gives the sample mean.")
g("4.1", "bayes-vs-frequentist", "Which statement correctly contrasts Bayesian and frequentist approaches?",
  ["Bayesian methods give parameters probability distributions", "Frequentist methods need a prior for every parameter", "Bayesian methods produce point estimates only", "Frequentist methods treat parameters as random"],
  "A", "Bayesians express uncertainty about parameters with priors and posteriors; frequentists treat parameters as fixed and data as random.")
g("4.1", "covariance", "How does correlation relate to covariance?",
  ["It is covariance scaled by both standard deviations", "It is covariance multiplied by the sample size", "It is the square root of the covariance", "It is covariance divided by the variance of x"],
  "A", "r = cov(x, y) / (sd_x × sd_y), which makes it unit-free and bounded between −1 and 1.")
g("4.1", "coefficient-interpretation", "In a linear regression of house price (£) on floor area (m²) and other features, the floor area coefficient is 2,500. What does this mean?",
  ["Each extra m² adds about £2,500, holding others fixed", "Every house in the data costs at least £2,500", "Floor area explains 2,500 units of price variance", "Prices rise by 2,500% for each extra square metre"],
  "A", "A coefficient is the expected change in the outcome for a one-unit change in that predictor, with the others held constant.")
g("4.1", "markov", "A Markov chain is a model in which:",
  ["The next state depends only on the current state", "Every state is equally likely at every step", "States are chosen to maximise a reward", "The next state depends on all past states equally"],
  "A", "The Markov property ('memorylessness') underpins customer-journey, credit-rating and queue models.")
g("4.1", "median-calc", "What is the median of 3, 9, 4, 7, 100?",
  ["7", "24.6", "4", "9"],
  "A", "Sorted: 3, 4, 7, 9, 100, so the median is 7. The mean is 24.6, pulled up by the outlier.")
g("4.1", "continuous-probability", "For a continuous random variable, the probability of it taking any single exact value is:",
  ["Zero", "One", "The height of the density curve", "The mean of the distribution"],
  "A", "Probabilities for continuous variables come from areas under the density curve over intervals, not from single points.")

b("4.1", "broad-claims-time", "An insurer wants to know whether a new claims process changed average settlement time, using samples before and after. Which TWO steps are appropriate?",
  ["Check the distribution of times, which is likely skewed", "Use a suitable test or interval for the difference", "Report only the larger of the two sample means", "Assume normality without looking at the data"],
  "AB", "Durations are usually right-skewed, so check the shape and choose a test (e.g. Mann–Whitney or a t-test on logs) and report an interval.")
b("4.1", "broad-energy-demand", "An energy company models monthly electricity demand. Which TWO techniques suit this data?",
  ["Time-series decomposition into trend and seasonality", "Regression on temperature and calendar features", "K-means clustering of the monthly totals only", "A chi-squared test of the monthly values"],
  "AB", "Demand has trend and strong seasonal and weather effects; decomposition and regression with explanatory features capture them.")

# =========================== 4.2 =========================================
g("4.2", "explore-exploit", "In reinforcement learning, the trade-off between trying new actions and repeating actions known to work is:",
  ["Exploration versus exploitation", "Bias versus variance", "Precision versus recall", "Training versus inference"],
  "A", "Too little exploration misses better actions; too much wastes reward. Epsilon-greedy and bandit algorithms balance the two.")
g("4.2", "rl-policy", "In reinforcement learning, a 'policy' is:",
  ["The agent's rule for choosing actions in each state", "The reward the environment returns after an action", "The record of all states visited so far", "The data used to pre-train the agent"],
  "A", "The policy maps states to actions; learning aims to find the policy that maximises long-run reward.")
g("4.2", "generative-models", "Which TWO are types of generative model?",
  ["Generative adversarial networks (GANs)", "Diffusion models", "K-means clustering", "Logistic regression"],
  "AB", "Generative models learn to produce new data resembling the training data; k-means and logistic regression do not generate data.")
g("4.2", "feature-store", "A feature store is used to:",
  ["Share consistent features between training and serving", "Store trained model weights for each version", "Archive raw data in low-cost object storage", "Hold the labels used to evaluate the model"],
  "A", "Feature stores prevent training–serving skew and let teams reuse features. Model weights belong in a model registry.")
g("4.2", "canary-release", "Releasing a new model to a small share of traffic before full rollout is called:",
  ["A canary release", "A blue-green rebuild", "A cold start", "A rollback"],
  "A", "Canary releases limit the impact of a bad model; shadow deployments run a model without using its outputs.")
g("4.2", "shadow-deployment", "Running a new model alongside the current one on live data, without acting on its outputs, is:",
  ["Shadow deployment", "Canary release", "A/B testing", "Batch scoring"],
  "A", "Shadow mode compares predictions safely before any user is affected; A/B tests and canaries do expose some users.")
g("4.2", "rag-vs-finetune", "A chatbot must answer from a company's policies, which change every month. Which approach is usually best?",
  ["Retrieval-augmented generation over current documents", "Fine-tuning the model each month on the documents", "Training a new language model from scratch", "Prompting the base model with no documents"],
  "A", "RAG grounds answers in up-to-date documents with sources; fine-tuning suits style or format, not frequently changing facts.")
g("4.2", "automl", "AutoML tools mainly automate:",
  ["Model selection and hyperparameter tuning", "Collecting and labelling training data", "Defining the business problem to solve", "Explaining results to stakeholders"],
  "A", "AutoML searches algorithms and settings; framing, data quality and communication still need people.")
g("4.2", "llm-agents", "An LLM 'agent' differs from a simple chatbot mainly because it:",
  ["Can plan steps and call tools to complete a task", "Is trained from scratch for each new user", "Has no limit on the length of its context", "Is immune to producing made-up output"],
  "A", "Agents combine an LLM with tools (search, code, APIs) and multi-step planning; they still hallucinate and need guardrails.")
g("4.2", "bayesian-optimisation", "Bayesian optimisation for hyperparameter tuning:",
  ["Uses past results to choose promising settings next", "Tries every combination on a fixed grid", "Samples settings uniformly at random", "Picks the settings with the best training accuracy"],
  "A", "A surrogate model of performance guides the search, so fewer expensive training runs are needed than grid or random search.")

b("4.2", "broad-loan-default", "A bank wants to predict loan default and must explain decisions to customers. Which TWO approaches fit?",
  ["An interpretable model, or a complex one explained with tools like SHAP", "Evaluation with precision, recall and fairness checks across groups", "Accuracy alone as the measure of success, as defaults are rare", "A model trained once and then left running without monitoring"],
  "AB", "Explainability, suitable metrics for imbalanced outcomes, fairness checks and monitoring are all expected for credit decisions.")
b("4.2", "broad-recommender-process", "A streaming service wants to recommend shows and keep improving them. Which sequence is most sensible?",
  ["Define success, build a simple baseline, then iterate and monitor", "Build the most complex model first, then decide what success means", "Deploy random recommendations, then stop once users complain", "Copy a competitor's model without measuring it on your own data"],
  "A", "Clear success metrics and a baseline make improvements measurable; monitoring catches drift after launch.")

# =========================== 4.3 =========================================
g("4.3", "word2vec", "Word2vec learns word embeddings by:",
  ["Predicting words from their neighbouring words", "Counting word frequencies in each document", "Assigning each word a random fixed vector", "Sorting words by their part of speech"],
  "A", "Skip-gram and CBOW train a shallow network on context prediction, so words in similar contexts get similar vectors.")
g("4.3", "bleu", "Which metric is commonly used to evaluate machine translation against reference translations?",
  ["BLEU", "ROUGE", "IoU", "AUC"],
  "A", "BLEU measures n-gram precision against references; ROUGE is recall-oriented and mainly used for summaries.")
g("4.3", "intent-classification", "A customer chatbot decides whether a message is about billing, delivery or returns. This task is:",
  ["Intent classification", "Named entity recognition", "Machine translation", "Text summarisation"],
  "A", "Intent classification routes messages; NER then extracts details such as order numbers or dates.")
g("4.3", "unet", "Which architecture is widely used for image segmentation, with an encoder–decoder shape and skip connections?",
  ["U-Net", "LSTM", "Word2vec", "Naive Bayes"],
  "A", "U-Net was designed for medical image segmentation and is now used widely for pixel-level labelling.")
g("4.3", "vision-transformer", "A Vision Transformer (ViT) processes an image by:",
  ["Splitting it into patches treated like tokens", "Reading it one pixel at a time in sequence", "Converting it to text with OCR first", "Clustering its pixels with k-means"],
  "A", "Patches are embedded and passed through self-attention layers, as words are in text transformers.")
g("4.3", "detection-vs-recognition", "What is the difference between face detection and face recognition?",
  ["Detection finds faces; recognition identifies whose face it is", "Detection identifies the person; recognition finds the face", "Detection works on video; recognition works on photos", "Detection needs labels; recognition needs none at all"],
  "A", "Recognition processes biometric data, which raises much greater legal and ethical issues than detection.")
g("4.3", "image-resize", "Before photos of different sizes are fed into a CNN, they are usually:",
  ["Resized to a fixed input size", "Converted into word embeddings", "Sorted by file size on disk", "Saved as plain text files"],
  "A", "Most CNNs expect a fixed input shape; images are resized or cropped and then normalised.")

b("4.3", "broad-call-transcripts", "A telecoms company has thousands of call transcripts and wants to know why customers complain. Which TWO approaches fit?",
  ["Topic modelling or clustering to find themes", "Text classification using a labelled sample", "Optical character recognition on the text", "Semantic segmentation of the transcripts"],
  "AB", "Unsupervised methods discover themes; a labelled sample allows reliable classification and measurement of each theme.")
b("4.3", "broad-shelf-cameras", "A supermarket wants to detect empty shelves from store cameras. Which TWO considerations matter most?",
  ["Labelled images covering varied stores and lighting", "Privacy of shoppers who appear in the footage", "The number of words printed on each product name", "The font style used on the shelf-edge price labels"],
  "AB", "Representative training data drives accuracy; footage of people is personal data, so privacy controls are needed.")

# =========================== 4.4 =========================================
g("4.4", "cost-per-prediction", "A cloud endpoint costs £2 per hour and serves 4,000 predictions per hour. What is the cost per 1,000 predictions?",
  ["£0.50", "£2.00", "£8.00", "£0.05"],
  "A", "£2 ÷ 4 = £0.50 per 1,000. Unit costs like this make it easy to compare serving options.")
g("4.4", "push-down", "Why push filtering and aggregation into the database rather than pulling every row into Python?",
  ["Less data is moved and the database is built for it", "Python's pandas library has no grouping functions", "Database licences are charged per row returned", "It removes the need for indexes on the tables"],
  "A", "Pushing work to where the data lives cuts network transfer and memory use and uses the database's optimiser.")
g("4.4", "retrain-frequency", "Retraining a model daily costs ten times more than monthly, but accuracy barely changes. What does this suggest?",
  ["Monthly retraining is likely the better trade-off", "Daily retraining is needed to prevent overfitting", "The model should be retrained every hour instead", "Retraining frequency has no effect on cost"],
  "A", "Retrain as often as drift requires and no more; monitoring shows when performance actually degrades.")
g("4.4", "team-capacity", "A team of two must support five models in production. Which TWO choices reduce the burden most?",
  ["Standardise on shared tooling and templates", "Automate monitoring and alerting", "Use a different framework for each model", "Retrain each model by hand when asked"],
  "AB", "Consistency and automation let a small team support more models; bespoke stacks and manual work don't scale.")
g("4.4", "good-enough", "A simple rule catches nearly as many fraud cases as a complex model at a fraction of the cost. What should decide between them?",
  ["Value of the extra catches against cost and risk", "Whichever approach is more technically impressive", "The complex model, as accuracy should come first", "The rule, as simple methods should be preferred"],
  "A", "Compare the marginal value with total cost of ownership, explainability and maintenance; neither choice is automatic.")

b("4.4", "broad-churn-six-weeks", "A small team must deliver a customer churn model in six weeks with a limited cloud budget. Which TWO choices are most sensible?",
  ["Start with a simple, well-understood model as a baseline", "Use batch scoring rather than an always-on real-time service", "Train a large deep network from scratch on GPUs", "Build custom infrastructure before any modelling"],
  "AB", "Time, budget and skills constraints favour simple baselines and cheap batch deployment.")
b("4.4", "broad-llm-or-inhouse", "When choosing between an LLM API and an in-house model for classifying customer emails, which TWO factors should be weighed?",
  ["Cost per request at the expected volume", "Data protection rules on sending emails outside", "The model's popularity on social media", "How recently the vendor's logo was updated"],
  "AB", "Volume-driven cost and information governance are key constraints alongside accuracy and latency.")

# =========================== 4.5 =========================================
g("4.5", "test-pyramid", "The 'test pyramid' recommends:",
  ["Many fast unit tests, fewer integration tests, few end-to-end tests", "Mostly end-to-end tests, as they test the whole system", "Equal numbers of unit, integration and end-to-end tests", "Manual testing first, then automating it much later"],
  "A", "Unit tests are fast and pinpoint failures; end-to-end tests are slower and more brittle, so fewer are used.")
g("4.5", "arrange-act-assert", "Arrange–Act–Assert describes:",
  ["A common structure for writing a unit test", "The three stages of a CI/CD pipeline", "A branching strategy for Git repositories", "The steps of a formal code review"],
  "A", "Arrange the inputs, act by calling the code, assert the result – a clear pattern for readable tests.")
g("4.5", "trunk-based", "In trunk-based development, developers:",
  ["Merge small changes into the main branch often", "Keep long-lived feature branches for months", "Commit directly to the production servers", "Release once a year from a release branch"],
  "A", "Frequent small merges with CI reduce painful merge conflicts; GitFlow uses longer-lived develop and release branches.")
g("4.5", "git-tag", "Which Git feature marks a specific commit as release v1.2.0?",
  ["A tag", "A stash", "A fork", "A hook"],
  "A", "Tags give commits permanent, readable names, often matching semantic version numbers.")
g("4.5", "refactoring", "Refactoring means:",
  ["Restructuring code without changing what it does", "Adding new features to the existing code", "Rewriting the code in another programming language", "Removing all comments from the codebase"],
  "A", "Good tests make refactoring safe by confirming behaviour is unchanged.")
g("4.5", "code-smells", "Which TWO are common 'code smells' that suggest refactoring?",
  ["Duplicated code in several places", "Very long functions with many parameters", "Descriptive variable and function names", "Small modules with a single purpose"],
  "AB", "Duplication and long functions make code hard to change safely; the other two are signs of healthy code.")
g("4.5", "sphinx", "Which tool generates documentation websites from Python docstrings?",
  ["Sphinx", "Black", "pytest", "pip"],
  "A", "Sphinx (or MkDocs with plugins) builds documentation; Black formats, pytest tests, pip installs packages.")

b("4.5", "broad-notebook", "A team's key analysis is a 2,000-line notebook run by hand by one person. Which TWO changes most improve its reliability?",
  ["Move logic into version-controlled, tested modules", "Run it automatically in a pipeline, not by hand", "Add more notebook cells for each new request", "Email copies of the notebook to the team weekly"],
  "AB", "Version control, tests and automation (the RAP approach) remove single points of failure and manual error.")
b("4.5", "broad-merge-checks", "Before merging a change to a shared data pipeline, which TWO checks should normally pass?",
  ["Automated tests in continuous integration", "Review by another team member", "Approval from every report's end users", "A manual re-run of last year's results"],
  "AB", "CI tests and peer review are the standard quality gates for shared code.")

# =========================== 5.1 =========================================
g("5.1", "commercial-data", "Which TWO are key considerations when buying third-party commercial data?",
  ["Licence terms on how the data may be used and shared", "How the supplier collected the data, and its quality", "Whether the file names follow your conventions", "Whether the data arrives as a single file"],
  "AB", "Licensing and provenance determine whether the data can be used and trusted.")
g("5.1", "clickstream", "Records of the pages a user visits and the buttons they click on a website are called:",
  ["Clickstream data", "Reference data", "Master data", "Survey data"],
  "A", "Clickstream (behavioural event) data is high-volume and semi-structured; consent rules for cookies may apply.")
g("5.1", "cc-licence", "Data released under a Creative Commons Attribution (CC BY) licence can be:",
  ["Reused and adapted if the source is credited", "Used for personal study only, not shared", "Viewed online but not copied or shared", "Reused only by registered non-profit groups"],
  "A", "CC BY, like the OGL, allows reuse including commercially with attribution; 'NC' variants forbid commercial use.")
g("5.1", "internal-external", "Which is an example of an internal data source for a retailer?",
  ["Its own till transaction records", "National census statistics", "Competitors' published prices", "Social media posts about the brand"],
  "A", "Internal sources come from the organisation's own systems; the others are external.")
g("5.1", "public-datasets", "When using a public dataset from a site such as Kaggle to inform a business decision, what is the main caution?",
  ["Its origin and fit for your context may be unclear", "It will be too large to load into pandas", "It is likely to contain only synthetic data", "It needs a paid licence for any analysis"],
  "A", "Check provenance, documentation, licence and how representative it is before relying on it.")
g("5.1", "transactional-systems", "Which data source records each sale, payment or booking as it happens?",
  ["A transactional (OLTP) system", "A data catalogue", "A survey platform", "A reference data table"],
  "A", "Operational transactional systems capture business events; analysts usually access them via replicas or warehouses.")

b("5.1", "broad-bookings-fall", "A travel firm wants to understand why bookings fell. Which TWO data sources would most directly help?",
  ["Its own booking and website analytics data", "Customer feedback and survey responses", "National census population counts", "A competitor's annual report from 2015"],
  "AB", "Behavioural data shows what changed; feedback helps explain why. The others are distant or out of date.")
b("5.1", "broad-data-broker", "Before using a dataset bought from a data broker, which TWO questions matter most?",
  ["Was personal data collected lawfully, with a valid basis?", "Do the licence terms allow your intended use?", "Is the file name consistent with your conventions?", "Does the broker use the same database as you?"],
  "AB", "Lawful basis and licence terms decide whether you can use the data at all.")

# =========================== 5.2 =========================================
g("5.2", "lossy-images", "Why is JPEG a poor choice for storing images used to train a model that detects fine scratches?",
  ["Lossy compression can remove fine detail", "JPEG files are unreadable by Python", "JPEG stores the pixels as plain text", "JPEG supports only black and white"],
  "A", "JPEG is lossy; PNG or TIFF are lossless and keep every pixel value.")
g("5.2", "sparse-matrix", "A document–term matrix has 50,000 columns, but each row has only a few non-zero values. How is it usually stored?",
  ["As a sparse matrix", "As a dense array", "As a CSV file", "As a JSON array of rows"],
  "A", "Sparse formats store only non-zero entries, saving huge amounts of memory.")
g("5.2", "hash-table", "Python dictionaries give fast lookup by key because they are implemented as:",
  ["Hash tables", "Linked lists", "Sorted arrays", "Binary heaps"],
  "A", "Hashing gives average O(1) lookup, versus O(n) for scanning a list.")
g("5.2", "orc", "ORC, like Parquet, is a:",
  ["Columnar file format for analytics", "Row-based format for message streams", "Markup language for documents", "Compression algorithm for images"],
  "A", "ORC and Parquet are both columnar formats from the Hadoop ecosystem; Avro is row-based.")
g("5.2", "schema-registry", "In a streaming platform, a schema registry is used to:",
  ["Store and check the schemas producers and consumers use", "Keep the full history of every message sent", "Encrypt messages between producers and consumers", "Balance load across the partitions of a topic"],
  "A", "Registries enforce compatible schema evolution, so producers can't break consumers.")
g("5.2", "tree-structure", "An organisation chart in which each employee has exactly one manager is best represented as a:",
  ["Tree (hierarchy)", "Flat list", "Time series", "Raster grid"],
  "A", "Trees are graphs with no cycles and one parent per node; in SQL they are often modelled with a self-referencing key.")

b("5.2", "broad-supplier-formats", "A company receives supplier data as emailed Excel files, a REST API and scanned PDFs. Which TWO steps help most?",
  ["Convert each source to a standard table with a defined schema", "Use OCR or table extraction for the scanned PDFs", "Keep each source in its original format for analysis", "Ask analysts to copy and paste values by hand"],
  "AB", "Standardising formats and extracting structure from unstructured inputs makes the data usable and repeatable.")
b("5.2", "broad-app-events", "Logs from a mobile app arrive as nested JSON events, millions per day. Which TWO choices suit analysis?",
  ["Flatten the events into tables", "Store them in a columnar format such as Parquet", "Paste them into a spreadsheet each morning", "Convert each event into a PDF for archiving"],
  "AB", "Flattening plus columnar storage makes large semi-structured data efficient to query.")

# =========================== 5.3 =========================================
g("5.3", "label-noise", "Training labels were assigned inconsistently by different annotators. This is known as:",
  ["Label noise", "Data drift", "Zero-inflation", "Heaping"],
  "A", "Label noise limits achievable accuracy; clear guidelines and agreement checks reduce it.")
g("5.3", "entry-errors", "A customer age column contains values of 999 and 0, and some ages entered as birth years. Which TWO actions are appropriate?",
  ["Define valid ranges and flag values outside them", "Trace and fix systematic entry errors, such as years", "Average the invalid values with the valid ones", "Leave them in, as they will cancel each other out"],
  "AB", "Validation rules and fixing systematic errors at source are standard cleaning steps.")
g("5.3", "irregular-sampling", "Readings arrive at irregular intervals, sometimes seconds apart and sometimes hours. What is a common first step before time-series modelling?",
  ["Resample to a regular interval", "Delete readings closer than an hour", "Sort the readings by their value", "Treat each reading as a new series"],
  "A", "Resampling (with suitable aggregation and gap handling) gives the regular index most time-series methods need.")
g("5.3", "default-values", "A date-of-birth field shows a large spike on 1 January 1900. The most likely cause is:",
  ["A system default used when the date is unknown", "A genuine cluster of very old customers", "Seasonality in when customers sign up", "A time zone conversion error"],
  "A", "Default or placeholder values masquerade as real data; treat them as missing.")
g("5.3", "s-curve", "Adoption of a new product rises slowly, then rapidly, then levels off. This S-shaped pattern is:",
  ["Logistic (saturating) growth", "Linear growth over time", "Exponential decay", "A random walk process"],
  "A", "Exponential-looking early growth often saturates; extrapolating it naively over-forecasts.")
g("5.3", "cohort-analysis", "Comparing customers grouped by the month they joined, to see how retention changes over time, is:",
  ["Cohort analysis", "Seasonal adjustment", "Outlier detection", "Sensitivity analysis"],
  "A", "Cohorts separate changes in customer quality from changes over customer lifetime.")

b("5.3", "broad-ecommerce-checks", "Before training a model on two years of e-commerce transactions, which TWO checks are most important?",
  ["Look for missing values, duplicates and outliers", "Check for seasonality and recording changes over time", "Confirm the CSV file names are in lower case", "Check that the data fits on one screen"],
  "AB", "Data quality issues and non-stationarity are the most common causes of misleading models.")
b("5.3", "broad-gym-app", "A gym chain finds members who use its app more have lower cancellation rates. Which TWO explanations should be considered alongside a causal effect?",
  ["Already committed members may both use the app and stay", "Members about to leave may stop using the app first", "App use is measured in minutes rather than in hours", "The app is designed with a dark colour scheme"],
  "AB", "Confounding (commitment) and reverse causation are common in observational real-world data.")


for _k in TITLES:
    QUESTIONS.extend(_gap[_k][1])
    QUESTIONS.extend(_broad[_k][1])
