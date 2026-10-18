from ._helpers import make_builder

q, QUESTIONS = make_builder("5.2", "Data formats, structures and data delivery methods, including unstructured data")

# --- Structured / semi / unstructured ----------------------------------------------
q("structure-types", "JSON and XML files are usually classed as:",
  ["Structured data", "Semi-structured data", "Unstructured data", "Relational data"],
  "B", "They have self-describing keys/tags and hierarchy but no rigid tabular schema.")
q("structure-types", "Which TWO are examples of unstructured data?",
  ["Free-text customer reviews", "Photographs from insurance claims", "A JSON feed of sensor readings", "A CSV of order records"],
  "AB", "Unstructured data lacks a predefined data model; JSON is semi-structured and CSV is structured.")
q("structure-types", "A relational database table with defined columns and data types is an example of:",
  ["Structured data", "Semi-structured data", "Unstructured data", "Streaming data"],
  "A", "Structured data conforms to a fixed schema of rows and typed columns.")
q("unstructured-processing", "Which TWO techniques are used to extract structure from unstructured data?",
  ["NLP such as entity extraction or text classification", "Computer vision or OCR applied to images and scans", "Normalising a relational schema to third normal form", "Partitioning a table by date for faster queries"],
  "AB", "Unstructured content needs NLP/CV/speech processing to turn it into analysable features.")

# --- File formats ------------------------------------------------------------------
q("csv-pitfalls", "Which TWO are common pitfalls of CSV files?",
  ["No embedded data types, so dates and numbers may be misread", "Delimiters or line breaks inside fields need correct quoting", "Files are binary, so they need special tools to open", "Nested records are stored natively and must be flattened"],
  "AB", "CSV is simple, plain-text and flat but untyped; quoting, encoding and delimiter issues are common.")
q("parquet", "Why is Apache Parquet popular for analytical workloads?",
  ["It is a row-based text format that is easy to inspect by eye", "It is a compressed columnar format that stores its schema", "It is a row-based binary format designed for message streams", "It is an in-memory format shared between processes"],
  "B", "Columnar layout plus compression and stored schema make analytical reads efficient. Row-based binary for streams describes Avro; in-memory describes Arrow.")
q("avro", "Apache Avro is commonly used in streaming pipelines (e.g. with Kafka) because it:",
  ["Is a row-based binary format with a schema that supports evolution", "Is a columnar format that lets queries read only selected fields", "Is a human-readable text format that needs no schema at all", "Is a multidimensional array format for gridded scientific data"],
  "A", "Avro suits record-at-a-time serialisation with evolving schemas. Columnar describes Parquet; gridded arrays describe NetCDF.")
q("json-xml", "Which statement about JSON vs XML is generally true?",
  ["JSON maps naturally to objects; XML uses tags and supports XSD schemas", "XML maps naturally to objects; JSON uses tags and supports XSD schemas", "JSON supports attributes on elements; XML does not support arrays", "XML is the default for modern web APIs; JSON is mainly for config"],
  "A", "Both represent hierarchy; JSON dominates modern web APIs.")
q("nested-json", "An API returns deeply nested JSON. What is a common first step before tabular analysis in pandas?",
  ["Flatten it, e.g. with `pandas.json_normalize`", "Convert it to XML and parse with an XSD", "Load it as a single text column and use regex", "Pivot it from long to wide format with `pivot`"],
  "A", "Flattening turns hierarchical records into a table, possibly producing several related tables.")
q("encoding", "Text such as 'cafÃ©' appearing instead of 'café' most likely indicates:",
  ["A character encoding mismatch", "A delimiter inside a quoted field", "A floating-point rounding error", "A corrupted compression stream"],
  "A", "Mojibake arises when UTF-8 bytes are decoded as e.g. Latin-1; specify the encoding explicitly.")
q("spatial-formats", "Which TWO are formats commonly used for vector geospatial data (points, lines, polygons)?",
  ["GeoJSON", "Shapefile", "GeoTIFF", "NetCDF"],
  "AB", "GeoTIFF is raster and NetCDF is gridded/array data; GeoJSON, Shapefile and GeoPackage store vector features.")
q("raster-vector", "A satellite image of land surface temperature, stored as a grid of cells, is an example of:",
  ["Raster data", "Vector data", "Point data", "Network data"],
  "A", "Raster = grid of cells/pixels; vector = discrete geometries.")
q("netcdf", "Which format is widely used for multidimensional scientific data such as climate model outputs (time × latitude × longitude × variable)?",
  ["NetCDF", "GeoJSON", "Avro", "Shapefile"],
  "A", "NetCDF (and HDF5) store self-describing multidimensional arrays efficiently.")
q("pickle", "Why should you not load a Python pickle file from an untrusted source?",
  ["Unpickling can execute arbitrary code", "Pickles silently lose numeric precision", "Pickles are tied to one operating system", "Pickles store data without compression"],
  "A", "Pickle deserialisation is not secure; prefer formats such as Parquet or JSON for exchange.")
q("excel-pitfalls", "Which TWO are known risks of using Excel for data processing?",
  ["Automatic type conversion, e.g. IDs to dates or lost leading zeros", "A row limit of 1,048,576 that can silently truncate data", "Numbers stored with less than single-precision accuracy", "Text limited to ASCII characters in each worksheet cell"],
  "AB", "Excel's conversions and limits have caused high-profile data losses; it uses double precision and supports Unicode.")
q("dates", "Which date format is the international standard that sorts correctly as text and avoids day/month ambiguity?",
  ["YYYY-MM-DD", "DD/MM/YYYY", "MM/DD/YYYY", "DD-Mon-YYYY"],
  "A", "ISO 8601 (YYYY-MM-DD) is unambiguous and sorts correctly as text.")
q("fixed-width", "In a fixed-width text file:",
  ["Each field occupies set character positions on every line", "Each field is separated by a tab or other delimiter", "Each record is stored as a self-describing object", "Each line has the same number of fields but varies in width"],
  "A", "Parsing requires a specification of the column positions.")
q("compression", "Compressing a large text file with gzip mainly trades:",
  ["Smaller size for CPU time to compress and decompress", "Smaller size for some loss of precision in values", "Faster queries for a larger file on disk", "Easier editing for slower network transfer"],
  "A", "gzip is lossless: it saves space and bandwidth at some compute cost.")
q("binary-serialisation", "Protocol Buffers (protobuf) is best described as:",
  ["A compact, schema-defined binary format for exchanging data", "A columnar file format for storing large analytical tables", "A human-readable markup language with tags and attributes", "A streaming platform for publishing and subscribing to events"],
  "A", "Binary formats are smaller and faster than JSON but not human-readable.")

# --- Structures --------------------------------------------------------------------------
q("tidy-data", "According to 'tidy data' principles, which TWO statements are true?",
  ["Each variable forms a column", "Each observation forms a row", "Each time period forms a column", "Each table holds all entity types"],
  "AB", "Tidy data: variables in columns, observations in rows, one type of observational unit per table.")
q("long-wide", "A table has columns site, 2022, 2023, 2024 containing annual readings. Converting it to columns site, year, reading is called:",
  ["Reshaping wide to long (melting)", "Reshaping long to wide (pivoting)", "Normalising to third normal form", "One-hot encoding the year column"],
  "A", "pandas `melt` turns wide data into long format, which suits most plotting and modelling tools.")
q("graph-structure", "Data describing connections between entities (e.g. users following other users) is naturally represented as:",
  ["A graph", "A raster", "A data cube", "A time series"],
  "A", "Graphs model relationships and networks as nodes and edges.")
q("data-types", "Why can storing a monetary amount as a binary floating-point number cause problems?",
  ["Some decimals can't be represented exactly", "Floats overflow above about one million", "Floats drop the sign of negative values", "Floats store at most two decimal places"],
  "A", "e.g. 0.1 + 0.2 ≠ 0.3 exactly; use decimal types or integer pence for money.")

# --- Delivery methods ---------------------------------------------------------------------
q("delivery", "Which TWO are push-based data delivery methods?",
  ["Webhooks that call your endpoint on events", "Message streams such as Kafka or Event Hubs", "Querying an API on a schedule (polling)", "Downloading a published file each month"],
  "AB", "Push sends data when available; polling and manual download are pull-based.")
q("delivery", "A supplier deposits a daily extract file on a secure server that you collect. This delivery method is best described as:",
  ["Batch file transfer", "Change data capture", "Event streaming", "Database replication"],
  "A", "Scheduled file drops (e.g. via SFTP) are a common batch delivery mechanism.")
q("message-queue", "What is a key benefit of using a message queue between a data producer and consumer?",
  ["It decouples them, buffering messages while the consumer catches up", "It ensures each message is processed in a single transaction", "It converts messages into a columnar format for analysis", "It stores the full history permanently for later querying"],
  "A", "Queues provide buffering, decoupling and reliability.")
q("schema-evolution", "A data provider adds a new optional field to its feed. What is this an example of?",
  ["Schema evolution", "Data normalisation", "Concept drift", "Schema-on-write"],
  "A", "Robust pipelines tolerate additive changes; data contracts help manage breaking ones.")
q("data-contract", "A data contract between a producer and consumer team typically specifies:",
  ["The schema, meaning, quality expectations and delivery SLAs", "The licence fees payable for each download of the dataset", "The infrastructure and cloud region used to host the data", "The dashboards and reports the consumer will build"],
  "A", "Contracts make expectations explicit and reduce breaking changes.")
q("api-formats", "Most modern web APIs return data in which format by default?",
  ["JSON", "XML", "CSV", "YAML"],
  "A", "JSON is lightweight and maps to native structures in most languages; XML is still used by older SOAP services.")
