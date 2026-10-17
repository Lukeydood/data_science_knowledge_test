from ._helpers import make_builder

q, QUESTIONS = make_builder("3.2", "Database systems: relational, data warehousing & OLAP, NoSQL and real-time; pros and cons")

# --- Relational fundamentals ------------------------------------------------
q("acid", "In ACID, what does Atomicity guarantee?",
  ["A transaction either completes in full or has no effect", "Committed changes survive a crash or power failure", "Concurrent transactions do not see each other's changes", "Data satisfies the defined rules and constraints"],
  "A", "Atomicity = all or nothing. Durability is surviving crashes, Isolation is non-interference, Consistency is rule satisfaction.")
q("acid", "Which ACID property ensures that once a transaction is committed, it will survive a power failure?",
  ["Atomicity", "Consistency", "Isolation", "Durability"],
  "D", "Durability means committed changes are persisted (e.g. via write-ahead logs) and survive crashes.")
q("acid", "Two users update the same bank balance at the same time; the database ensures the result is as if the transactions ran one after the other. Which property is this?",
  ["Isolation", "Durability", "Atomicity", "Consistency"],
  "A", "Isolation keeps concurrent transactions from seeing each other's intermediate state.")
q("normalisation", "What is the main purpose of normalising a relational database?",
  ["To reduce joins and speed up analytical queries", "To reduce redundancy and avoid update anomalies", "To enforce encryption of sensitive attributes", "To pre-aggregate measures for reporting"],
  "B", "Normalisation organises data so each fact is stored once, preventing anomalies; it usually adds joins, which is why warehouses often denormalise.")
q("normalisation", "A table is in 2NF and no non-key attribute depends on another non-key attribute. Which normal form has been reached?",
  ["First normal form (1NF)", "Third normal form (3NF)", "Fourth normal form (4NF)", "Second normal form only"],
  "B", "3NF removes transitive dependencies (non-key → non-key).")
q("keys", "What is a foreign key?",
  ["A column whose values uniquely identify each row of its table", "A column that references the primary key of another table", "A column indexed to speed up text searches on the table", "A column combined with others to form a composite key"],
  "B", "Foreign keys link tables and enforce referential integrity; the first option describes a primary key.")
q("sql-where-having", "Which SQL clause filters groups after aggregation, e.g. keeping only regions with more than 100 incidents?",
  ["WHERE", "HAVING", "GROUP BY", "QUALIFY"],
  "B", "WHERE filters rows before grouping; HAVING filters aggregated groups after GROUP BY. QUALIFY filters window-function results.")
q("sql-joins", "Which join returns all rows from the left table and matching rows from the right table, with NULLs where there is no match?",
  ["INNER JOIN", "LEFT OUTER JOIN", "FULL OUTER JOIN", "CROSS JOIN"],
  "B", "A LEFT JOIN keeps every left-hand row; a FULL OUTER JOIN keeps unmatched rows from both sides.")
q("indexes", "Which TWO are trade-offs of adding an index to a database table?",
  ["Faster lookups and filtering on the indexed columns", "Slower inserts and updates as the index is maintained", "Lower storage use because rows are stored compressed", "Fewer locks needed when many users write at once"],
  "AB", "Indexes speed reads but cost write performance and extra storage.")

# --- Warehousing & OLAP --------------------------------------------------------
q("oltp-olap", "Which statement correctly contrasts OLTP and OLAP systems?",
  ["OLTP serves many small transactions; OLAP serves complex queries over history", "OLTP serves complex queries over history; OLAP serves many small transactions", "OLTP is usually denormalised; OLAP is usually highly normalised to 3NF", "OLTP stores data by column; OLAP stores data by row for fast inserts"],
  "A", "OLTP (e.g. ordering systems) is write-heavy and normalised; OLAP (warehouses, cubes) is read-heavy and optimised for aggregation.")
q("star-schema", "In a star schema, what does the central fact table typically contain?",
  ["Descriptive attributes such as names and addresses", "Numeric measures plus keys to the dimension tables", "Hierarchies such as day, month, quarter and year", "Lookup values for codes used across the warehouse"],
  "B", "Facts hold measurable events and keys; dimensions hold descriptive context and hierarchies (who, what, where, when).")
q("star-schema", "How does a snowflake schema differ from a star schema?",
  ["It stores facts at a coarser level of aggregation", "Its dimensions are normalised into sub-dimension tables", "It links several fact tables through shared dimensions", "Its fact table holds descriptive text, not measures"],
  "B", "Snowflaking normalises dimensions, saving space but adding joins. Several facts sharing dimensions is a 'galaxy' or fact constellation.")
q("denormalisation", "Why are data warehouse dimension tables often deliberately denormalised?",
  ["To reduce joins and speed up read-heavy queries", "To reduce storage by removing repeated values", "To enforce referential integrity between tables", "To support many concurrent single-row updates"],
  "A", "Analytical workloads favour fewer joins; the extra redundancy is an accepted trade-off.")
q("scd", "A customer changes address and the warehouse adds a new dimension row with start/end dates, keeping the old row. Which technique is this?",
  ["Slowly Changing Dimension Type 1", "Slowly Changing Dimension Type 2", "Slowly Changing Dimension Type 3", "Slowly Changing Dimension Type 0"],
  "B", "Type 2 adds a new row preserving full history; Type 1 overwrites; Type 3 keeps a 'previous value' column; Type 0 never changes.")
q("olap-ops", "An analyst views a sales cube for the year 2025 only, fixing one value of the time dimension. Which OLAP operation is this?",
  ["Roll-up", "Slice", "Drill-down", "Dice"],
  "B", "A slice fixes a single value on one dimension. A dice selects a sub-cube using conditions on several dimensions.")
q("olap-ops", "Moving from monthly totals to daily detail in an OLAP cube is called:",
  ["Roll-up", "Drill-down", "Slice", "Pivot"],
  "B", "Drill-down moves to finer granularity; roll-up aggregates to a coarser level.")
q("columnar", "Why are columnar storage engines well suited to analytical queries?",
  ["Each row is stored together, so single-row updates are cheap", "Only the needed columns are read and similar values compress well", "Every column is indexed automatically when a table is created", "Rows are held in insertion order, so time ranges are contiguous"],
  "B", "Analytical queries touch few columns over many rows; columnar layout minimises I/O and compresses efficiently.")
q("data-mart", "What is a data mart?",
  ["A catalogue for discovering datasets across the organisation", "A subject- or department-specific subset of a data warehouse", "A staging area where raw extracts land before transformation", "A read-only replica of an operational database for reporting"],
  "B", "Data marts serve a particular business area (e.g. finance) for simpler, faster access.")
q("kimball-inmon", "Which statement describes the Kimball approach to data warehousing?",
  ["Top-down: a normalised enterprise warehouse first, then marts", "Bottom-up: dimensional marts joined by conformed dimensions", "Raw data kept in a lake with schema applied only at query time", "Hubs, links and satellites modelled for auditable history"],
  "B", "Kimball is bottom-up dimensional modelling; Inmon is top-down with a normalised (3NF) warehouse; hubs/links/satellites is Data Vault.")
q("materialised-view", "What is a materialised view?",
  ["A saved query that is re-run each time it is used", "A stored query result that is refreshed periodically", "A temporary table dropped at the end of a session", "A diagram showing the relationships between tables"],
  "B", "Materialised views trade storage and freshness for query speed; an ordinary view is re-run each time.")
q("mpp", "Cloud data warehouses such as Azure Synapse, Amazon Redshift and Google BigQuery handle large queries mainly by:",
  ["Caching all tables in the memory of one large server", "Distributing data and query work across many nodes", "Storing rows in a B-tree optimised for point lookups", "Pre-computing every possible aggregate in an OLAP cube"],
  "B", "Massively parallel processing (MPP) splits data and query execution across many compute nodes.")

# --- NoSQL ------------------------------------------------------------------
q("nosql-types", "Which type of NoSQL database is best suited to querying relationships in a social network, such as 'friends of friends'?",
  ["Key-value store", "Graph database", "Wide-column store", "Document store"],
  "B", "Graph databases (e.g. Neo4j) store nodes and edges and traverse relationships efficiently.")
q("nosql-types", "A web application needs very fast lookup of user session data by session ID. Which database type is most appropriate?",
  ["Graph database", "Key-value store", "Wide-column store", "Document store"],
  "B", "Key-value stores (e.g. Redis) give sub-millisecond lookups by key and are commonly used for caches and sessions.")
q("nosql-types", "A product catalogue where each item has a different set of attributes, stored as JSON, best suits which database type?",
  ["Document store", "Key-value store", "Graph database", "Time-series database"],
  "A", "Document stores (e.g. MongoDB, Cosmos DB) handle flexible, nested records and let you query on fields inside them.")
q("nosql-types", "Which database type is designed for very high write throughput across many nodes, organising data by partition key and column families (e.g. Apache Cassandra)?",
  ["Wide-column store", "Graph database", "Document store", "Key-value store"],
  "A", "Wide-column stores distribute data by partition key for scale-out writes.")
q("nosql-pros-cons", "Which TWO are typical disadvantages of many NoSQL databases compared with relational databases?",
  ["Weaker support for complex joins and ad-hoc queries", "Eventual consistency can return stale reads", "Difficulty scaling beyond a single large server", "A rigid schema that is costly to change"],
  "AB", "NoSQL trades rich querying and strong consistency for scalability and flexibility; scaling limits and rigid schemas are typical of relational systems.")
q("nosql-pros-cons", "Which TWO are typical advantages of NoSQL databases?",
  ["Flexible schemas for varied or changing structures", "Horizontal scaling across many commodity servers", "Multi-table ACID transactions by default", "A single standard query language across products"],
  "AB", "Flexibility and scale-out are the core benefits; cross-record ACID and a common query standard are relational strengths.")
q("scaling", "Adding more servers to share the load, rather than upgrading a single server, is called:",
  ["Vertical scaling", "Horizontal scaling", "Replication lag", "Load shedding"],
  "B", "Horizontal scaling (scaling out) adds nodes; vertical scaling (scaling up) adds CPU/RAM to one machine.")
q("cap", "According to the CAP theorem, when a network partition occurs a distributed system must choose between:",
  ["Consistency and durability", "Consistency and availability", "Availability and latency", "Durability and partition size"],
  "B", "Partition tolerance is unavoidable in distributed systems, so during a partition you trade consistency against availability.")
q("base", "Which statement describes 'eventual consistency' (part of the BASE model)?",
  ["Every read returns the most recent committed write", "Replicas converge on the same value once updates stop", "Writes are rejected until all replicas acknowledge", "Each transaction is serialised against all others"],
  "B", "BASE = Basically Available, Soft state, Eventual consistency; replicas may be temporarily out of sync. The other options describe strong consistency.")
q("vector-db", "A RAG chatbot stores text embeddings and retrieves the passages most similar to a user's query. What kind of store is designed for this?",
  ["Vector database", "Graph database", "Key-value store", "Full-text inverted index"],
  "A", "Vector databases (e.g. Chroma, pgvector, Azure AI Search) index embeddings for nearest-neighbour similarity search. Inverted indexes match keywords, not meaning.")
q("time-series-db", "Which database type is optimised for timestamped measurements such as telemetry readings every minute?",
  ["Graph database", "Time-series database", "Document store", "OLAP cube"],
  "B", "Time-series databases (e.g. InfluxDB, TimescaleDB) optimise ingestion, compression and time-window queries.")

# --- Real-time approaches ---------------------------------------------------------
q("kafka", "What is Apache Kafka primarily used for?",
  ["Running distributed SQL queries over files in a lake", "Publishing and subscribing to durable streams of events", "Scheduling and orchestrating batch data pipelines", "Caching query results in memory for web applications"],
  "B", "Kafka stores ordered, replicated logs of events (topics) that producers write and consumers read. Orchestration is e.g. Airflow; SQL-on-files is e.g. Trino.")
q("cdc", "Change Data Capture (CDC) is a technique that:",
  ["Copies the entire source database to the target each night", "Propagates inserts, updates and deletes from a source as they occur", "Compares row checksums between source and target every week", "Records who viewed each row for audit and compliance purposes"],
  "B", "CDC streams changes incrementally (often from the transaction log), reducing load and latency compared with full extracts.")
q("lambda-kappa", "The Lambda architecture for big data combines:",
  ["A batch layer for complete history and a speed layer for low-latency views", "A single streaming pipeline that replays the log to rebuild history", "Serverless functions triggered by each new file landing in storage", "A transactional database replicated to a read-only analytics copy"],
  "A", "Lambda = batch + speed + serving layers. Kappa (second option) simplifies by using one streaming pipeline for everything.")
q("windowing", "In stream processing, a tumbling window of 5 minutes:",
  ["Starts every minute and covers the previous 5 minutes", "Groups events into fixed, non-overlapping 5-minute blocks", "Closes after 5 minutes with no events from that user", "Holds the most recent 5 events regardless of time"],
  "B", "Tumbling windows are fixed and non-overlapping; sliding/hopping windows overlap; session windows close after inactivity.")
q("in-memory", "What is the main trade-off of an in-memory database?",
  ["Very fast access, but RAM is costly and needs persistence for restarts", "Very cheap storage, but queries are slower than on disk-based systems", "Strong durability, but it is limited to key-value access patterns", "Large capacity, but it does not enforce relational constraints"],
  "A", "In-memory systems are fast but RAM is limited and volatile, so snapshots/logs are needed for durability.")
