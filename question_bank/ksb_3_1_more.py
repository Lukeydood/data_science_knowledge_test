from ._helpers import make_builder

q, QUESTIONS = make_builder("3.1", "Data processing and storage, including on-premise and cloud technologies", start=101)

q("availability-zones", "In public cloud, what is an availability zone?",
  ["A physically separate data centre within one region", "A geographic area containing several cloud regions", "A storage tier with a contractual uptime level", "A network boundary that isolates one customer's resources"],
  "A", "Regions contain multiple availability zones (separate facilities with independent power and networking); spreading across zones protects against one site failing.")
q("sla-maths", "A cloud service has a 99.9% monthly availability SLA. Roughly how much downtime does that allow in a 30-day month?",
  ["About 4 minutes", "About 43 minutes", "About 7 hours", "About 3 days"],
  "B", "0.1% of 30 × 24 × 60 = 43.2 minutes. 99.99% would allow about 4 minutes.")
q("egress", "A team is surprised by a large cloud bill after downloading terabytes of results to on-premise servers. What is the most likely cause?",
  ["Data egress charges", "Data ingress charges", "Reserved instance fees", "Storage tier rehydration"],
  "A", "Providers usually charge for data leaving their network (egress); ingress is typically free.")
q("encryption", "Which TWO are standard protections for data held in cloud storage?",
  ["Encryption at rest", "Encryption in transit (TLS)", "Storing it in a public bucket", "Disabling access logging"],
  "AB", "Encrypt stored data and data moving over networks; public buckets and no logging are common causes of breaches.")
q("least-privilege", "Granting a pipeline's service identity only read access to the one container it needs follows which principle?",
  ["Least privilege", "Defence in depth", "Separation of duties", "Zero data retention"],
  "A", "Least privilege limits the damage if an identity is compromised. Defence in depth layers several controls.")
q("iac", "Defining cloud resources such as storage accounts and clusters in version-controlled code (e.g. Terraform, Bicep) is called:",
  ["Infrastructure as code", "Platform as a service", "Continuous integration", "Configuration drift"],
  "A", "IaC makes environments repeatable, reviewable and easy to rebuild; configuration drift is what happens without it.")
q("orchestration", "A tool such as Apache Airflow or Azure Data Factory is mainly used to:",
  ["Schedule and coordinate dependent pipeline tasks", "Store large files cheaply in tiered object storage", "Run interactive SQL queries over a data lake", "Train and register machine learning models"],
  "A", "Orchestrators run tasks in the right order (often as a DAG), handle retries and alert on failure.")
q("dag", "In pipeline orchestration, a DAG is:",
  ["A directed acyclic graph of tasks and dependencies", "A distributed array of GPUs used for model training", "A data access gateway between cloud regions", "A daily aggregation of logs from every task"],
  "A", "Directed: dependencies have a direction; acyclic: no loops, so there is always a valid order to run tasks.")
q("idempotency", "Why should a data pipeline step be idempotent?",
  ["Re-running it gives the same result, so retries are safe", "It runs faster because earlier results are cached in memory", "It can run on any cloud without code changes", "It processes each record in parallel across nodes"],
  "A", "Idempotent steps (e.g. overwrite a partition rather than append) can be retried after failure without duplicating data.")
q("small-files", "A data lake contains millions of tiny files, and queries over it are slow. What is the usual fix?",
  ["Compact them into fewer, larger files", "Move them all into the archive tier", "Convert them from Parquet to CSV", "Spread them across more storage accounts"],
  "A", "Each file adds metadata and open overhead; compaction into larger files (often 128 MB–1 GB) speeds scans.")
q("spark-lazy", "In Apache Spark, transformations such as `filter` and `select` are lazy. What does this mean?",
  ["They are only executed when an action such as `count` is called", "They are executed immediately on a single driver node", "They are cached in memory after their first execution", "They are executed in the order they were written, one at a time"],
  "A", "Spark builds a plan and optimises it, executing only when an action needs a result.")
q("spark-shuffle", "Why are operations that cause a 'shuffle' in Spark (e.g. large joins, groupBy) often slow?",
  ["Data must be redistributed across the network between nodes", "They can only run on a single partition at a time", "They force all intermediate data to be written to the archive tier", "They disable the query optimiser for the whole job"],
  "A", "Shuffles move data between executors over the network and often spill to disk; minimising them is a key optimisation.")
q("mapreduce", "In the MapReduce model, what does the reduce phase do?",
  ["Aggregates all values that share the same key", "Splits input files into blocks across the nodes", "Applies a function to each input record independently", "Replicates outputs to protect against node failure"],
  "A", "Map emits key-value pairs per record; shuffle groups them by key; reduce aggregates each key's values.")
q("data-virtualisation", "Querying data where it lives in several source systems, without first copying it into a central store, is called:",
  ["Data virtualisation", "Data replication", "Extract, transform, load", "Change data capture"],
  "A", "Virtualisation gives a unified view without moving data, at the cost of depending on source performance.")
q("time-travel", "Table formats such as Delta Lake and Apache Iceberg support 'time travel'. What does this allow?",
  ["Querying a table as it was at an earlier version", "Moving data automatically to cheaper storage over time", "Scheduling queries to run at a future time", "Replaying a stream of events in real time"],
  "A", "Versioned table metadata lets you audit changes, reproduce analyses and roll back mistakes.")
q("cold-start", "A serverless function occasionally takes several seconds to respond after a quiet period. This is known as:",
  ["A cold start", "Throttling", "Back-pressure", "A memory leak"],
  "A", "When no warm instance exists, the platform must start a new one, adding latency.")
q("cost-management", "Which TWO practices help control cloud costs?",
  ["Tagging resources by project and setting budget alerts", "Shutting down or auto-scaling idle compute", "Choosing the largest instance size by default", "Keeping every dataset in the hot storage tier"],
  "AB", "Visibility (tags, budgets) and right-sizing are the main levers on cloud spend.")
q("dr-strategies", "A disaster recovery approach where a scaled-down copy of the system runs in a second region, ready to scale up, is:",
  ["Warm standby", "Backup and restore", "Cold storage", "Active-passive DNS"],
  "A", "From cheapest/slowest to dearest/fastest: backup and restore, pilot light, warm standby, active-active.")
q("latency-throughput", "What is the difference between latency and throughput?",
  ["Latency is time per request; throughput is work done per unit time", "Latency is work done per unit time; throughput is time per request", "Latency measures storage size; throughput measures network speed", "Latency applies to batch jobs; throughput applies to streaming jobs"],
  "A", "A system can have high throughput but high latency (big batches), or low latency but low throughput.")
q("kubernetes", "Kubernetes is mainly used to:",
  ["Deploy, scale and manage containers across a cluster", "Build container images from a Dockerfile", "Store the version history of infrastructure-as-code files", "Provide a managed data warehouse service"],
  "A", "Kubernetes orchestrates containers (scheduling, scaling, self-healing); Docker builds images.")
q("nas-san", "An organisation's on-premise storage area network (SAN) provides servers with:",
  ["Block-level storage over a dedicated network", "File shares accessed over standard SMB or NFS", "Object storage accessed through an HTTP API", "Tape-based archives for long-term retention"],
  "A", "SANs provide block storage; NAS devices provide file-level shares over SMB/NFS.")
q("managed-identity", "Rather than storing a password in code, an Azure function accesses storage using an identity issued and rotated by the platform. This is a:",
  ["Managed identity", "Shared access key", "Service account password", "Personal access token"],
  "A", "Managed identities remove the need to handle secrets in code at all.")
q("data-lifecycle", "A storage lifecycle policy that moves blobs to the cool tier after 30 days and deletes them after 7 years helps with:",
  ["Cost and retention management", "Query performance and indexing", "Encryption and key rotation", "Replication and failover"],
  "A", "Lifecycle rules automate tiering and deletion in line with retention schedules.")
q("on-prem-scenarios", "Which TWO situations most favour keeping a workload on-premise?",
  ["Strict rules require data to stay on equipment the organisation controls", "Very low-latency links are needed to on-site laboratory instruments", "Demand is highly variable with occasional very large peaks", "The team wants to avoid managing hardware and patching"],
  "AB", "Control and locality favour on-premise; spiky demand and offloaded maintenance favour cloud.")
q("compute-storage", "A key architectural feature of modern cloud warehouses such as Snowflake and BigQuery is that:",
  ["Compute and storage are separated and scale independently", "Compute and storage are tied together on each cluster node", "All data is held in memory on a single large node", "Each query runs on a dedicated physical server"],
  "A", "Separating storage from compute lets you scale query power up or down without moving data.")
