from ._helpers import make_builder

q, QUESTIONS = make_builder("5.2", "Data formats, structures and data delivery methods, including unstructured data", start=101)

q("json-types", "Which TWO are native JSON value types?",
  ["Array", "Boolean", "Date", "Decimal"],
  "AB", "JSON has string, number, boolean, null, object and array; dates are usually ISO 8601 strings.")
q("jsonl", "Why is JSON Lines (one JSON object per line) popular for large logs and data exports?",
  ["Records can be streamed and processed line by line", "It compresses better than any binary format", "It enforces a strict schema on each line of the file", "It can be opened directly as an Excel sheet"],
  "A", "Each line is independent, so files can be appended, split and processed without loading them whole.")
q("yaml", "YAML is most commonly used for:",
  ["Human-readable configuration files", "Columnar storage of large tables", "Binary messages exchanged between services", "Multidimensional climate arrays"],
  "A", "YAML (e.g. CI workflows, Kubernetes manifests) favours readability; indentation matters.")
q("xml-parsing", "Which approach is best for extracting values from a well-formed XML document?",
  ["An XML parser with XPath queries", "Regular expressions over the raw text", "Splitting the text on every comma", "Converting it to an image for OCR"],
  "A", "Parsers handle nesting, namespaces and escaping correctly; regex breaks easily on XML.")
q("arrow", "Apache Arrow is best described as:",
  ["An in-memory columnar format shared between tools", "A row-based file format for writing logs to disk", "A schema language for describing REST API endpoints", "A compression algorithm designed for text files"],
  "A", "Arrow lets pandas, Polars, DuckDB, Spark etc. exchange data with little or no copying.")
q("delta-iceberg", "Delta Lake and Apache Iceberg add what on top of Parquet files in a data lake?",
  ["A transaction log enabling ACID updates and versioning", "A graphical interface for browsing images in storage", "An encryption layer that replaces cloud key management", "A REST API that converts every file into JSON"],
  "A", "Open table formats track which files make up each table version.")
q("excel-format", "Which TWO problems commonly arise when receiving data as Excel workbooks from partners?",
  ["Merged cells and multi-row headers", "Several tables or notes placed on one sheet", "Too few rows to analyse with confidence", "Files that open only in R and not in Python"],
  "AB", "Spreadsheets designed for people often need careful parsing or a request for a tidy extract.")
q("encoding-bom", "A CSV opens with strange characters `ï»¿` before the first column name. What is the likely cause?",
  ["A UTF-8 byte order mark read with the wrong encoding", "A missing delimiter at the end of the header row", "A corrupted gzip compression header on the file", "A trailing newline at the very end of the file"],
  "A", "Read with `encoding='utf-8-sig'` to strip the BOM.")
q("delimiter", "A 'CSV' from a European system uses semicolons as separators and commas as decimal points. How should it be read in pandas?",
  ["read_csv with sep=';' and decimal=','", "read_csv with its default settings", "read_json with orient='records'", "read_excel with header=None"],
  "A", "Locale conventions vary; specify the delimiter and decimal separator explicitly.")
q("geopackage", "Which open format stores vector and raster spatial data in a single SQLite-based file and is often recommended over shapefiles?",
  ["GeoPackage", "GeoTIFF", "KML", "CSV with WKT"],
  "A", "GeoPackage avoids shapefile limits such as 10-character field names and multiple sidecar files.")
q("crs", "Two spatial datasets don't line up on a map even though they cover the same area. What is the most likely cause?",
  ["They use different coordinate reference systems", "One file uses tabs as separators and the other uses commas", "One dataset contains more attribute columns", "They were saved with different file extensions"],
  "A", "e.g. British National Grid (EPSG:27700) vs WGS84 (EPSG:4326); reproject to a common CRS.")
q("wkt", "`POINT (-2.58 51.45)` is an example of which representation?",
  ["Well-Known Text (WKT) geometry", "A JSON object with two numeric keys", "A GeoTIFF raster cell", "A UPRN property identifier"],
  "A", "WKT is a text format for geometries; WKB is its binary form.")
q("time-zones", "Sensor timestamps are stored in local UK time without a time zone. What problem can occur?",
  ["Ambiguous or missing hours at clock changes", "Values become rounded to the nearest minute", "Readings are automatically converted to GMT", "Dates are sorted in reverse order by default"],
  "A", "Store timestamps in UTC (or with offset) and convert for display.")
q("unix-time", "A column contains values such as 1767225600. This is most likely:",
  ["A Unix timestamp in seconds", "An Excel serial date number", "A UK postcode stored as a number", "A latitude multiplied by one million"],
  "A", "Unix epoch seconds; Excel serial dates are much smaller numbers (days since 1900).")
q("leading-zeros", "Identifiers such as '01234' lose their leading zero after loading. How should this be prevented?",
  ["Read the column as text (string dtype)", "Multiply the column by ten after loading", "Sort the column before saving it again", "Convert the column to floating point"],
  "A", "IDs are labels, not numbers; read them as strings.")
q("nested-structure", "Each permit record contains a list of conditions of varying length. Which TWO tabular representations are reasonable?",
  ["A separate conditions table linked by permit ID", "An exploded long table with one row per condition", "Fixed columns condition_1 … condition_500", "Concatenating everything into one cell"],
  "AB", "Normalise or explode nested lists; wide fixed columns and concatenation are hard to analyse.")
q("audio-video", "Which TWO are typical first steps to make audio recordings analysable?",
  ["Transcribe speech to text", "Extract features such as spectrograms", "Open the files in a spreadsheet", "Sort files by colour"],
  "AB", "Unstructured media must be converted to text or numeric features.")
q("pdf-extraction", "Tables need to be extracted from hundreds of PDF reports. Which TWO factors most affect the approach?",
  ["Whether the PDFs contain a text layer or are scanned images", "Whether table layouts are consistent across reports", "The number of pages printed on each sheet of paper", "The author's choice of font colour for headings"],
  "AB", "Text PDFs suit table extractors; scanned PDFs need OCR; inconsistent layouts need more robust methods.")
q("sftp", "Why is SFTP preferred to plain FTP for transferring data files between organisations?",
  ["It encrypts both credentials and data in transit", "It transfers files faster by skipping integrity checksums", "It converts files to Parquet during transfer", "It does not require any login credentials"],
  "A", "Plain FTP sends credentials and data unencrypted.")
q("api-vs-file", "Which TWO are advantages of receiving data via an API rather than periodic file dumps?",
  ["Data can be fetched on demand, so it is fresher", "Clients can request filtered subsets", "Authentication is not usually needed for APIs", "Schemas are fixed and do not change between versions"],
  "AB", "APIs give fresher, selective access but still require auth and versioning.")
q("api-versioning", "A provider changes its API URL from /v1/ to /v2/ with a different response structure. What does this practice provide?",
  ["Old clients keep working on v1 while others migrate", "Faster responses for every client still using v1", "Automatic conversion of v1 clients' code", "Removal of the need for API documentation"],
  "A", "Versioning lets breaking changes happen without immediately breaking consumers.")
q("pub-sub", "In a publish–subscribe system, how do producers and consumers relate?",
  ["Producers publish to a topic; many subscribers can receive", "Each producer sends directly to exactly one consumer", "Consumers must poll every producer for new data", "Producers wait until all consumers confirm receipt"],
  "A", "Pub/sub decouples senders and receivers; Kafka, Service Bus topics and Pub/Sub implement it.")
q("data-share", "Rather than copying data, a cloud warehouse lets a partner query a live, read-only view of selected tables. This is:",
  ["Secure data sharing", "Batch file transfer", "Database sharding", "Schema evolution"],
  "A", "Features like Snowflake/Delta Sharing avoid duplicate copies and stale extracts.")
q("bulk-vs-incremental", "A provider offers both a full snapshot and a daily file of changes. Which TWO are appropriate uses?",
  ["Load the snapshot, then apply daily changes", "Reload the snapshot periodically to reconcile", "Ignore the deletes listed in the change files", "Load only the change files from day one onwards"],
  "AB", "Initial full load plus incremental changes, with occasional reconciliation, is a standard pattern.")
