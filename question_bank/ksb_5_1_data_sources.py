from ._helpers import make_builder

q, QUESTIONS = make_builder("5.1", "Sources of data: files, operational systems, databases, web services, open/government data, news and social media")

q("primary-secondary", "Data collected by your own team through a bespoke field survey for the current project is:",
  ["Primary data", "Secondary data", "Administrative data", "Open data"],
  "A", "Primary data is collected first-hand for the purpose at hand; secondary data was collected by others for another purpose.")
q("primary-secondary", "Which TWO are examples of secondary data?",
  ["Census statistics published by the ONS", "Historical exchange rates from a public API", "Interviews your team conducts for this study", "Readings from sensors your team installs for this trial"],
  "AB", "Secondary data is reused from other collectors; the last two are primary.")
q("rest-api", "In a REST API, which HTTP method is conventionally used to retrieve data without changing it?",
  ["GET", "POST", "PUT", "PATCH"],
  "A", "GET is safe and idempotent; POST creates, PUT/PATCH update, DELETE removes.")
q("http-status", "An API call returns HTTP status 429. What does this indicate?",
  ["The requested resource was not found", "Too many requests have been sent", "The server hit an internal error", "Authentication credentials are missing"],
  "B", "429 signals rate limiting; back off and retry later (often using the Retry-After header).")
q("http-status", "Which HTTP status code indicates the requested resource was not found?",
  ["200", "301", "404", "403"],
  "C", "200 OK, 301 moved permanently, 403 forbidden, 404 not found.")
q("http-status", "An API returns 401 Unauthorized. What is the most likely cause?",
  ["Missing or invalid authentication credentials", "Valid credentials without permission for the resource", "The request body is malformed and fails to parse", "The client has exceeded its allowed request rate"],
  "A", "401 means authentication is required or has failed; 403 means authenticated but not permitted; 400 is a bad request; 429 is rate limiting.")
q("pagination", "An API returns 100 records per response but the dataset has 50,000 records. What must the client handle?",
  ["Pagination", "Rate limiting", "Authentication", "Content negotiation"],
  "A", "Paginated APIs return results in pages using page numbers, offsets or continuation tokens.")
q("web-scraping", "Which TWO considerations apply before scraping data from a website?",
  ["The site's terms of service and robots.txt", "Copyright, data protection and server load", "Whether the HTML uses semantic tags", "Whether the site is served over HTTPS"],
  "AB", "Scraping raises legal and ethical issues; prefer official APIs or open data where available. Markup and HTTPS are technical details.")
q("open-data", "Data published under the Open Government Licence (OGL) can generally be:",
  ["Used for non-commercial purposes only, with attribution", "Copied, adapted and used commercially, with attribution", "Used by public sector bodies only, without attribution", "Viewed and cited, but not adapted or redistributed"],
  "B", "The OGL is a permissive licence similar to CC BY: reuse, including commercially, with attribution.")
q("open-data", "Which TWO are examples of UK open/government data sources?",
  ["data.gov.uk", "Office for National Statistics", "Companies' internal HR systems", "Commercial credit reference agencies"],
  "AB", "Public bodies publish open datasets, e.g. data.gov.uk, ONS and Environment Agency APIs. The others are private or licensed.")
q("operational-systems", "Why is it usually inadvisable to run heavy analytical queries directly against a live operational (OLTP) system?",
  ["They can slow the business transactions it supports", "Operational data is too out of date for analysis", "Analytical SQL is not supported on OLTP databases", "Operational systems store data in a columnar format"],
  "A", "Use replicas, extracts or a warehouse to protect operational performance.")
q("operational-systems", "Data extracted from a CRM or case-management system for analysis is an example of:",
  ["Administrative data", "Experimental data", "Survey data", "Synthetic data"],
  "A", "Administrative data is collected through running a service, not designed for research.")
q("admin-data", "Which TWO are common limitations of administrative data used for analysis?",
  ["Definitions and coverage reflect operational needs", "Recording practices change over time", "Sample sizes are usually too small", "It is expensive to collect for each study"],
  "AB", "Admin data is a by-product of processes, so definitions, coverage and practices vary; it is typically large and cheap to reuse.")
q("social-media", "Which TWO are key limitations of using social media data to measure public opinion?",
  ["Users are not representative of the population", "Bots and coordinated campaigns distort signals", "Posts are too short to analyse with NLP", "Timestamps are not available for posts"],
  "AB", "Social media is a self-selected, noisy sample; access is also governed by platform terms.")
q("news-data", "When using news articles as a data source, which is an important consideration?",
  ["Editorial selection and framing shape what is reported", "Articles are usually too long for text analysis", "Publication dates are often missing or unreliable", "News text is mostly numeric and needs no NLP"],
  "A", "Newsworthiness biases what gets reported and how.")
q("sensor-data", "Which TWO are common issues with IoT/sensor data?",
  ["Gaps from device or communication outages", "Calibration drift over time", "Too few readings to support analysis", "Values recorded only as free text"],
  "AB", "Sensor data needs quality control for gaps, spikes, drift and clock errors; volume is usually high.")
q("survey-data", "A survey receives responses mostly from people with strong opinions. This introduces:",
  ["Non-response bias", "Measurement bias", "Recall bias", "Interviewer bias"],
  "A", "If responders differ systematically from non-responders (self-selection), estimates are biased.")
q("anonymisation", "Under UK GDPR, how is pseudonymised data (names replaced by IDs, with a key held separately) treated?",
  ["It is anonymous, so UK GDPR no longer applies", "It is still personal data, as re-identification is possible", "It becomes special category data requiring extra conditions", "It is exempt if the key is held by a different organisation"],
  "B", "Only truly anonymised data falls outside UK GDPR.")
q("provenance", "Recording where data came from, how it was transformed and by whom is known as:",
  ["Data lineage", "Data profiling", "Data cataloguing", "Data stewardship"],
  "A", "Lineage (provenance) supports trust, auditability and impact analysis. Profiling summarises content; a catalogue helps discovery.")
q("metadata", "Which is an example of metadata for a dataset?",
  ["Column descriptions, units, collection date and licence", "A random sample of rows used to check the contents", "Summary statistics calculated from each column", "Predictions made by a model trained on the data"],
  "A", "Metadata is 'data about data' that makes datasets understandable and reusable.")
q("fair", "The FAIR data principles state that data should be:",
  ["Findable, Accessible, Interoperable, Reusable", "Fair, Accurate, Integrated, Reliable", "Free, Anonymised, Indexed, Recorded", "Findable, Auditable, Integrated, Relevant"],
  "A", "FAIR principles guide good data stewardship.")
q("data-sharing", "Before receiving personal data from a partner organisation, what should normally be in place?",
  ["A data sharing agreement covering purpose, lawful basis and security", "A non-disclosure agreement signed by each analyst using the data", "Written consent from every individual named in the dataset", "A service level agreement covering delivery frequency and format"],
  "A", "Agreements document responsibilities and compliance; consent is only one possible lawful basis and often not the right one.")
q("identifiers", "Linking property-level datasets from different organisations is easier when they share:",
  ["A common unique identifier, such as the UPRN", "The same file format, such as CSV or Parquet", "The same update frequency and publication date", "A common coordinate reference system"],
  "A", "Stable shared identifiers avoid error-prone fuzzy matching on addresses.")
q("webhooks", "How does a webhook differ from polling an API?",
  ["The source pushes data to you when an event happens", "You request updates on a fixed schedule from the source", "The source sends a full extract file each night by SFTP", "You subscribe to a database replica that mirrors changes"],
  "A", "Webhooks are push-based, reducing latency and wasted requests; polling (second option) is pull-based.")
q("synthetic-data", "Which is a legitimate use of synthetic data?",
  ["Developing and testing pipelines without exposing real personal data", "Replacing real records in official statistics to protect privacy", "Filling gaps in real data before reporting the published figures", "Increasing the sample size to achieve statistical significance"],
  "A", "Synthetic data mimics real data's structure while reducing disclosure risk; it should not replace or pad real evidence.")
q("source-reliability", "Which TWO factors should be considered when assessing the reliability of a data source?",
  ["The authority and methodology of the publisher", "How current the data is and whether it is maintained", "How widely the dataset is shared and cited online", "How easy the data is to download and load into tools"],
  "AB", "Assess authority, methodology, currency, accuracy and coverage; popularity and convenience are not reliability.")
q("files", "Which TWO are risks when data is shared as ad-hoc files, such as emailed spreadsheets?",
  ["Multiple versions with no clear source of truth", "Undocumented manual edits introducing errors", "Files are too large to send by email", "Spreadsheets lack support for formulas"],
  "AB", "File-based sharing lacks version control and governance unless managed carefully.")
