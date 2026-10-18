from ._helpers import make_builder

q, QUESTIONS = make_builder("3.2", "Database systems: relational, data warehousing & OLAP, NoSQL and real-time; pros and cons", start=101)

q("sql-order", "In what logical order does a SQL engine evaluate these clauses?",
  ["FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY", "SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY", "FROM → GROUP BY → WHERE → SELECT → HAVING → ORDER BY", "SELECT → WHERE → FROM → HAVING → GROUP BY → ORDER BY"],
  "A", "This is why a column alias defined in SELECT usually can't be used in WHERE, but can be used in ORDER BY.")
q("sql-count", "What does `COUNT(column)` return compared with `COUNT(*)`?",
  ["The number of non-NULL values in that column", "The number of distinct values in that column", "The number of rows including NULLs in that column", "The number of columns in the result set"],
  "A", "COUNT(*) counts rows; COUNT(col) skips NULLs; COUNT(DISTINCT col) counts distinct non-NULL values.")
q("sql-null", "Why does `WHERE region = NULL` return no rows?",
  ["Comparisons with NULL evaluate to unknown, not true", "NULL values are filtered out before the WHERE clause is evaluated", "The = operator is only valid for numeric columns", "NULL must be written in lower case to match"],
  "A", "Use `IS NULL` / `IS NOT NULL`; three-valued logic means `= NULL` is never true.")
q("window-functions", "Which SQL feature calculates a running total or rank across rows while keeping each row in the result?",
  ["Window functions, e.g. SUM() OVER (ORDER BY date)", "GROUP BY with an aggregate such as SUM()", "A correlated subquery placed in the WHERE clause", "A UNION ALL of several aggregated queries"],
  "A", "Window functions compute over a set of rows related to the current row without collapsing them, unlike GROUP BY.")
q("union", "What is the difference between UNION and UNION ALL?",
  ["UNION removes duplicate rows; UNION ALL keeps them", "UNION keeps duplicate rows; UNION ALL removes them", "UNION joins on keys; UNION ALL joins on all columns", "UNION sorts the result; UNION ALL leaves it unsorted"],
  "A", "UNION ALL is faster because it skips de-duplication.")
q("cte", "A Common Table Expression (CTE), written with WITH, is mainly used to:",
  ["Name a subquery so a complex query is easier to read", "Store query results permanently for use in later sessions", "Enforce referential integrity between two tables", "Create an index that speeds up the main query"],
  "A", "CTEs improve readability and allow recursion; they are not persisted (unlike tables or materialised views).")
q("composite-key", "A table recording which staff attended which training session uses (staff_id, session_id) together as its primary key. This is a:",
  ["Composite key", "Surrogate key", "Foreign key", "Candidate index"],
  "A", "A composite key uses more than one column to uniquely identify a row.")
q("surrogate-key", "Why do data warehouses commonly use surrogate keys in dimension tables?",
  ["They are stable integer keys independent of source-system IDs", "They reuse the business identifiers from the source systems directly", "They encrypt the natural key to protect personal data", "They allow facts to be stored without any dimensions"],
  "A", "Surrogate keys insulate the warehouse from source key changes and support SCD Type 2 history.")
q("grain", "When designing a fact table, what does 'declaring the grain' mean?",
  ["Stating exactly what one row of the fact table represents", "Choosing the compression level for the fact table", "Listing the users allowed to query the fact table", "Deciding how often the fact table will be refreshed from source"],
  "A", "e.g. 'one row per water sample per determinand'. Grain decisions drive which dimensions and measures fit.")
q("additive-measures", "Which measure is semi-additive: it can be summed across some dimensions but not across time?",
  ["An account balance", "A sales amount", "A count of incidents", "A quantity of items sold"],
  "A", "Balances and stock levels add across accounts or sites but not across days (use the latest or average instead).")
q("conformed-dimension", "A 'Date' dimension shared with the same meaning by several fact tables across the warehouse is a:",
  ["Conformed dimension", "Degenerate dimension", "Junk dimension", "Role-playing fact"],
  "A", "Conformed dimensions allow consistent analysis across business processes (the Kimball bus architecture).")
q("star-vs-3nf", "Which TWO statements about star schemas compared with 3NF models are true?",
  ["Star schemas need fewer joins for typical analytical queries", "Star schemas are easier for business users to understand", "Star schemas store less redundant data than 3NF", "Star schemas are better for high-volume transactional writes"],
  "AB", "Star schemas trade redundancy for simpler, faster reads; 3NF suits transactional writes.")
q("molap-rolap", "How does ROLAP differ from MOLAP?",
  ["ROLAP queries relational tables; MOLAP uses pre-computed cubes", "ROLAP uses pre-computed cubes; MOLAP queries relational tables", "ROLAP works only in memory; MOLAP works only on disk", "ROLAP supports drill-down; MOLAP supports only slicing"],
  "A", "MOLAP is fast for pre-aggregated queries but less flexible; ROLAP scales to large detail data. HOLAP mixes both.")
q("sharding", "Splitting a large database table across several servers by a key such as customer ID is called:",
  ["Sharding", "Mirroring", "Normalising", "Indexing"],
  "A", "Sharding (horizontal partitioning across servers) enables scale-out but complicates cross-shard queries.")
q("replication-lag", "A read replica of a database shows slightly out-of-date data. This is called:",
  ["Replication lag", "Write amplification", "Lock contention", "Index fragmentation"],
  "A", "Asynchronous replicas trail the primary, so reads from them can be stale.")
q("locking", "Two transactions each wait for a lock held by the other, so neither can proceed. This is a:",
  ["Deadlock", "Dirty read", "Phantom read", "Lost update"],
  "A", "Databases detect deadlocks and roll back one transaction so the other can continue.")
q("isolation-anomaly", "A transaction reads data written by another transaction that has not yet committed. This anomaly is a:",
  ["Dirty read", "Phantom read", "Deadlock", "Write skew"],
  "A", "Dirty reads are prevented from the READ COMMITTED isolation level upwards.")
q("document-modelling", "In a document database, when is embedding related data inside a parent document usually a good choice?",
  ["When the related data is read together and has bounded size", "When the related data is shared by many different parent documents", "When the related data grows without any practical limit", "When the related data is updated independently and often"],
  "A", "Embed for data accessed together and bounded; reference (link) data that is shared, unbounded or updated independently.")
q("key-design", "In a wide-column store such as Cassandra, why is choosing the partition key so important?",
  ["It decides data distribution and which queries are efficient", "It decides which columns are encrypted at rest on each node", "It decides the order in which backups are taken and restored", "It decides which users can access each table"],
  "A", "Queries should target a partition key; poor keys create hot spots or require expensive scans.")
q("polyglot", "Using a relational database for transactions, a document store for a product catalogue and a search engine for text search in one system is called:",
  ["Polyglot persistence", "Data virtualisation", "Lambda architecture", "Master data management"],
  "A", "Each store is chosen for the workload it suits best, at the cost of more operational complexity.")
q("search-engine", "Which store is designed for fast full-text search with relevance ranking over large collections of documents?",
  ["Elasticsearch / OpenSearch", "PostgreSQL with B-tree indexes", "Redis key-value store", "Neo4j graph database"],
  "A", "Search engines use inverted indexes and relevance scoring (e.g. BM25).")
q("event-time", "In stream processing, why distinguish event time from processing time?",
  ["Events can arrive late or out of order, so results should use when they happened", "Processing time is more reliable because it is set by the processing server", "Event time matters for batch jobs but is ignored in stream windows", "Processing time determines the order of records in the source system"],
  "A", "Using event time with watermarks gives correct windowed results despite delays.")
q("delivery-semantics", "Which message delivery guarantee means a message is never lost but may be processed more than once?",
  ["At-least-once", "At-most-once", "Exactly-once", "Best-effort"],
  "A", "At-least-once requires consumers to be idempotent or de-duplicate; at-most-once may lose messages.")
q("stream-db", "Which TWO technologies are commonly used for real-time analytics on streaming data?",
  ["Apache Flink or Spark Structured Streaming", "Azure Stream Analytics or Kafka Streams", "A nightly SSIS package loading a warehouse", "A monthly CSV export emailed to analysts"],
  "AB", "Stream processors compute continuously over unbounded data; nightly and monthly loads are batch.")
q("htap", "A database designed to handle both transactional and analytical workloads on the same data is described as:",
  ["HTAP", "OLTP", "MPP", "ROLAP"],
  "A", "HTAP systems reduce the need to copy data to a separate warehouse, though usually at higher cost.")
