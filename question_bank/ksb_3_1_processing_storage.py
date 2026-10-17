from ._helpers import make_builder

q, QUESTIONS = make_builder("3.1", "Data processing and storage, including on-premise and cloud technologies")

# --- Cloud service models -------------------------------------------------
q("cloud-models", "In which cloud service model does the customer manage the operating system and applications, while the provider manages the physical servers, storage and networking?",
  ["Software as a Service (SaaS)", "Infrastructure as a Service (IaaS)", "Platform as a Service (PaaS)", "Function as a Service (FaaS)"],
  "B", "IaaS provides virtualised compute, storage and networking; the customer is responsible for the OS, middleware, runtime and applications.")
q("cloud-models", "A team uses a managed database where the cloud provider patches the operating system and database engine, and the team only manages schemas and data. Which service model is this?",
  ["Infrastructure as a Service (IaaS)", "Software as a Service (SaaS)", "Platform as a Service (PaaS)", "Colocation hosting"],
  "C", "Managed databases (e.g. Azure SQL Database, Amazon RDS) are PaaS: the platform is managed for you and you manage what you build on it.")
q("cloud-models", "Microsoft 365 and Gmail, where users simply use a finished application over the internet, are examples of which service model?",
  ["Software as a Service (SaaS)", "Platform as a Service (PaaS)", "Infrastructure as a Service (IaaS)", "Function as a Service (FaaS)"],
  "A", "SaaS delivers a complete application; the customer manages only their data and user settings.")
q("serverless", "Which TWO statements describe serverless computing (e.g. Azure Functions, AWS Lambda)?",
  ["Billing is typically per execution or compute time used", "You size and patch the virtual machines the code runs on", "Capacity scales automatically in response to events", "Code runs continuously on a reserved, dedicated host"],
  "AC", "Serverless abstracts servers away: billing is per invocation/compute-time and scaling is automatic. Servers still exist but you don't manage them.")

# --- Shared responsibility / sovereignty --------------------------------------
q("shared-responsibility", "Under the cloud shared responsibility model, who is normally responsible for classifying and controlling access to the data a customer uploads to an IaaS or PaaS service?",
  ["The cloud provider", "The customer", "The provider and an independent auditor", "The regional data protection authority"],
  "B", "Providers secure the cloud itself (physical, host, network); customers remain responsible for their data, identities and access configuration.")
q("data-sovereignty", "A UK public body must ensure personal data is held under UK jurisdiction. Which concept does this requirement relate to most directly?",
  ["Data lineage", "Data residency", "Data redundancy", "Data elasticity"],
  "B", "Data sovereignty/residency concerns the legal jurisdiction and physical location where data is stored and processed. Cloud providers address it through region selection.")

# --- On-prem vs cloud trade-offs -------------------------------------------
q("onprem-vs-cloud", "Which TWO are typical advantages of on-premise infrastructure over public cloud?",
  ["Direct physical control over hardware and data location", "Rapid scaling of capacity up and down on demand", "Lower cost for steady workloads on hardware already owned", "Hardware maintenance handled by an external provider"],
  "AC", "On-premise gives full control and can be cost-effective for stable workloads on owned kit; elastic scaling and offloaded maintenance are cloud advantages.")
q("capex-opex", "Migrating from on-premise servers to public cloud typically shifts IT spending in which way?",
  ["From operational to capital expenditure", "From capital to operational expenditure", "From variable to fixed annual licensing", "From pay-per-use to up-front purchasing"],
  "B", "Cloud replaces up-front hardware purchases (CapEx) with pay-as-you-go consumption (OpEx).")
q("elasticity", "A web service automatically adds compute instances during a flood-warning surge and removes them when demand falls. Which cloud characteristic is this?",
  ["Elasticity", "Durability", "Redundancy", "Portability"],
  "A", "Elasticity is the ability to automatically provision and de-provision resources to match demand.")
q("hybrid-cloud", "What best describes a hybrid cloud architecture?",
  ["Using services from two or more public cloud providers", "On-premise or private infrastructure integrated with public cloud", "A single provider offering both IaaS and PaaS services", "Containers and virtual machines on the same host"],
  "B", "Hybrid cloud integrates private/on-premise environments with public cloud. Using several public providers is 'multi-cloud'.")
q("vendor-lock-in", "Heavy use of one provider's proprietary managed services creates which main risk?",
  ["Loss of data residency", "Vendor lock-in", "Reduced elasticity", "Higher capital expenditure"],
  "B", "Proprietary APIs and services tie your architecture to one provider; mitigations include open formats, containers and abstraction layers.")
q("spot-instances", "What is the main trade-off of using spot / pre-emptible cloud instances?",
  ["Higher cost in return for a fixed uptime SLA", "Lower cost, but they can be reclaimed at short notice", "Lower cost, but they have reduced network bandwidth", "Higher cost in return for dedicated physical hardware"],
  "B", "Spot capacity is discounted spare capacity that can be interrupted, so it suits fault-tolerant batch jobs, not critical services.")

# --- Processing paradigms --------------------------------------------------
q("batch-vs-stream", "Which workload is best suited to batch processing rather than stream processing?",
  ["Flagging fraudulent card payments as they occur", "Producing the monthly payroll report", "Alerting when a river gauge exceeds a threshold", "Updating a live dashboard of website clicks"],
  "B", "Batch processing handles bounded datasets on a schedule where latency is not critical. The others require low-latency, continuous (stream) processing.")
q("batch-vs-stream", "Which TWO scenarios most need stream (real-time) processing?",
  ["Alerting on pumping-station telemetry that shows a failure", "Compiling the annual statutory accounts", "Detecting suspicious logins as they happen", "Building a quarterly archive of historic emails"],
  "AC", "Streaming is needed when value depends on reacting within seconds; periodic reporting and archiving are batch tasks.")
q("etl-elt", "What distinguishes ELT from ETL?",
  ["ELT transforms data in a staging server before loading it", "ELT loads raw data first and transforms it in the target", "ELT skips transformation and loads data unchanged", "ELT extracts data in real time using change capture"],
  "B", "ELT (Extract, Load, Transform) exploits scalable cloud warehouse compute to transform after loading; ETL transforms in a separate engine before loading.")
q("etl-elt", "In a classic ETL pipeline, where does transformation happen?",
  ["Inside the source operational system", "In a processing layer before loading", "Inside the target warehouse after loading", "In the reporting tool at query time"],
  "B", "ETL = Extract, Transform, Load: data is cleaned and reshaped in an intermediate engine before loading into the warehouse.")

# --- Storage types ----------------------------------------------------------
q("data-lake", "Which statement best describes a data lake?",
  ["A normalised relational store optimised for transactions", "A repository of raw data in native formats, read with schema-on-read", "A department-specific subset of a dimensional warehouse", "An in-memory store used to cache frequently read data"],
  "B", "Data lakes store structured, semi-structured and unstructured data cheaply in raw form; structure is applied when the data is read.")
q("schema-on-read", "Which pairing is correct?",
  ["Data warehouse: schema-on-read; data lake: schema-on-write", "Data warehouse: schema-on-write; data lake: schema-on-read", "Data warehouse and data lake: both schema-on-write", "Data warehouse and data lake: both schema-on-read"],
  "B", "Warehouses enforce a schema as data is loaded; lakes defer schema definition until query time.")
q("lakehouse", "A 'lakehouse' architecture (e.g. Delta Lake, Microsoft Fabric) aims to:",
  ["Move warehouse data back on-premise for lower latency", "Add warehouse features such as ACID tables to lake storage", "Replace object storage with an in-memory columnar cache", "Split the lake into separate departmental data marts"],
  "B", "Lakehouses add a transactional table format over open files in object storage, giving warehouse-like reliability on lake storage.")
q("object-storage", "Which TWO are characteristics of object storage (e.g. Azure Blob Storage, Amazon S3)?",
  ["Objects are stored with metadata and accessed by key via an HTTP API", "It is mounted as a raw low-latency disk for a VM's operating system", "It scales cheaply to very large volumes of unstructured data", "It is designed for frequent small in-place edits within a file"],
  "AC", "Object storage is a flat, API-accessed, massively scalable store. OS disks are block storage; objects are usually rewritten whole rather than edited in place.")
q("storage-types", "A virtual machine needs a low-latency disk for its operating system and database files. Which storage type is most appropriate?",
  ["Object storage", "Block storage", "Archive storage", "File share (SMB)"],
  "B", "Block storage presents raw volumes with low latency, suited to OS disks and databases.")
q("storage-tiers", "Data must be retained for 7 years for compliance but is very rarely accessed. Which storage tier is most cost-effective?",
  ["Hot tier", "Premium tier", "Archive tier", "Cool tier"],
  "C", "Archive tiers have the lowest storage cost but highest retrieval cost and latency, ideal for rarely accessed retained data. Cool suits infrequent but faster access.")

# --- Distributed processing -------------------------------------------------
q("hdfs", "How does HDFS (Hadoop Distributed File System) provide fault tolerance?",
  ["By mirroring each whole file to one standby server", "By replicating each block of a file across several nodes", "By storing parity data on a central RAID controller", "By taking a nightly snapshot to an off-site archive"],
  "B", "HDFS splits files into large blocks (128 MB default) and replicates them (default factor 3) across nodes so the loss of a node does not lose data.")
q("spark", "Why is Apache Spark usually faster than classic Hadoop MapReduce for iterative workloads such as machine learning?",
  ["It runs each job on a single larger machine", "It keeps intermediate data in memory between steps", "It compiles every job into optimised SQL queries", "It stores the data in a columnar file format"],
  "B", "MapReduce writes intermediate results to disk between stages; Spark's in-memory distributed datasets avoid that I/O for iterative algorithms.")
q("partitioning", "A large table of sensor readings is partitioned by date. What is the main benefit for queries filtered on a date range?",
  ["Duplicate readings are removed on write", "Partitions outside the range can be skipped", "Each partition is compressed more heavily", "Queries can run without any indexes at all"],
  "B", "Partition pruning means only the relevant partitions are scanned, reducing I/O and cost.")
q("containers", "How do containers (e.g. Docker) differ from virtual machines?",
  ["Each container runs its own full guest operating system", "Containers share the host OS kernel, so they are lighter", "Containers emulate hardware through a type-1 hypervisor", "Containers need a dedicated physical server per instance"],
  "B", "VMs virtualise hardware and each run a full OS; containers isolate processes while sharing the host kernel.")
q("edge-computing", "Remote river-level sensors have limited bandwidth, so readings are pre-processed on a device near the sensor before summaries are sent. This is an example of:",
  ["Edge computing", "Fog storage", "Data federation", "Vertical scaling"],
  "A", "Edge computing processes data close to its source to reduce latency and bandwidth.")

# --- Resilience -------------------------------------------------------------
q("rpo-rto", "What does the Recovery Point Objective (RPO) define?",
  ["The maximum acceptable time to restore the service", "The maximum acceptable data loss, measured in time", "The minimum number of backup copies to be kept", "The average time between successive failures"],
  "B", "RPO = how much data (in time) you can afford to lose; RTO = how long you can afford to be down; MTBF = mean time between failures.")
q("rpo-rto", "A service must be back online within 2 hours of a failure. Which metric is this?",
  ["Recovery Time Objective (RTO)", "Recovery Point Objective (RPO)", "Mean Time Between Failures (MTBF)", "Service Level Indicator (SLI)"],
  "A", "RTO is the target maximum downtime before service is restored.")
q("backup-321", "The '3-2-1' backup rule recommends:",
  ["3 daily, 2 weekly and 1 monthly backup", "3 copies, on 2 media types, 1 off-site", "3 replicas, in 2 regions, 1 cold standby", "3 years retention, 2 encryptions, 1 owner"],
  "B", "Three copies, two media types, one off-site protects against hardware failure, site loss and ransomware.")
q("replication", "What is the main purpose of geo-redundant storage replication?",
  ["To reduce write latency for users in other regions", "To keep data available if a whole region fails", "To reduce storage costs by moving cold data", "To keep data within a single legal jurisdiction"],
  "B", "Geo-replication protects against the loss of an entire data centre/region, at extra cost.")
