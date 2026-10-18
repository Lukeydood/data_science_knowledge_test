from ._helpers import make_builder

q, QUESTIONS = make_builder("5.1", "Sources of data: files, operational systems, databases, web services, open/government data, news and social media", start=101)

q("api-auth", "Which is the most common way to authenticate to a web API programmatically?",
  ["An API key or OAuth token sent in a request header", "A username and password typed into a browser pop-up each time", "A cookie copied manually from the developer's own browser", "An IP address written into the body of each request"],
  "A", "Keys/tokens in headers (e.g. `Authorization: Bearer …`) are standard; keep them out of URLs and code.")
q("query-params", "In `https://api.example.gov.uk/readings?station=E123&since=2026-01-01`, what are `station` and `since`?",
  ["Query parameters", "HTTP headers", "Path segments", "Request bodies"],
  "A", "Query parameters follow `?` and are separated by `&`; they typically filter or page results.")
q("http-post", "Which HTTP method is conventionally used to submit new data to create a resource?",
  ["POST", "GET", "HEAD", "OPTIONS"],
  "A", "POST creates; GET retrieves; HEAD gets headers only; OPTIONS describes allowed methods.")
q("status-5xx", "An API intermittently returns HTTP 503 Service Unavailable. What should a robust client do?",
  ["Retry later with exponential back-off", "Treat the data as permanently missing", "Change the request method to POST", "Resend the request immediately in a loop"],
  "A", "5xx errors are server-side and often transient; back-off avoids overwhelming the service.")
q("graphql", "How does a GraphQL API differ from a typical REST API?",
  ["The client specifies exactly which fields it wants in one query", "The server returns XML documents rather than JSON objects", "Every request must download the full dataset at once", "It can only be used for writing data, not reading it"],
  "A", "GraphQL avoids over- and under-fetching by letting clients shape the response.")
q("soap", "Older enterprise web services that exchange XML envelopes described by a WSDL file use:",
  ["SOAP", "REST", "gRPC", "WebSocket"],
  "A", "SOAP is a protocol with strict XML contracts; still found in legacy government and finance systems.")
q("database-connection", "Which TWO are good practices when an analysis connects directly to an organisational database?",
  ["Use a read-only account with minimal access", "Keep connection credentials in a secrets store", "Share one admin login across the whole analytics team", "Run full-table exports during peak business hours"],
  "AB", "Least privilege and secret management protect systems and data.")
q("odbc-jdbc", "ODBC and JDBC are:",
  ["Standard interfaces for connecting applications to databases", "File formats for exporting tables from spreadsheet tools", "Protocols for streaming events between microservices", "Licences that govern reuse of government data"],
  "A", "Drivers implementing ODBC/JDBC let tools such as Python, R or Power BI query many database engines.")
q("hydrology-api", "Many public transport operators publish near real-time departures and delays through:",
  ["A public open data API", "A paid commercial feed", "A weekly printed bulletin", "A members-only intranet"],
  "A", "Live transport, weather and similar feeds are commonly published as open data APIs, often under open licences such as the OGL.")
q("ons-data", "Which UK body is the main producer of official statistics such as the census and labour market data?",
  ["The Office for National Statistics", "The Information Commissioner's Office", "The Government Digital Service", "The National Audit Office"],
  "A", "ONS produces official statistics; ICO regulates data protection; NAO audits spending.")
q("official-stats", "Which TWO are typical strengths of official statistics as a data source?",
  ["Documented methods and quality information", "Consistent definitions, with revisions noted", "Updates every few seconds as live real-time feeds", "Coverage of named individuals' personal details"],
  "AB", "Official statistics prioritise documented, comparable methods; they are rarely real-time or record-level.")
q("data-revisions", "A published monthly figure is later changed as more complete data arrives. This is a:",
  ["Revision", "Retraction", "Restatement error", "Data breach"],
  "A", "Preliminary estimates are revised; analyses should record which vintage they used.")
q("geospatial-sources", "Which UK organisation is the national mapping agency providing authoritative geographic data?",
  ["Ordnance Survey", "Met Office", "Land Registry", "Natural England"],
  "A", "OS provides mapping and products such as AddressBase (with UPRNs); the Met Office provides weather data.")
q("weather-data", "To explain how the weather affects ice-cream sales, the most authoritative source is:",
  ["The Met Office", "Social media posts", "News reports", "A travel website"],
  "A", "Use authoritative observational datasets; secondary sources are incomplete and unverified.")
q("social-media-api", "Why has collecting large volumes of social media data become harder for researchers?",
  ["Platforms have restricted or begun charging for API access", "Social media posts are no longer stored with timestamps", "UK law now prohibits most analysis of public posts by researchers", "Most platforms have stopped allowing text posts"],
  "A", "Access changes by platforms mean research data pipelines can break; check terms and costs.")
q("sampling-social", "Social media posts mentioning a brand are used to estimate customer satisfaction across the UK. Which TWO biases are most likely?",
  ["Users skew younger and more urban", "A few highly active accounts dominate volume", "Every customer is equally likely to post about the brand", "Posts are spread evenly across the regions of the UK"],
  "AB", "Platform demographics and activity concentration both distort representativeness.")
q("news-api", "When building a dataset from news articles via an aggregator API, which TWO checks are important?",
  ["Removing duplicate syndicated copies of the same story", "Checking licence terms for storing full article text", "Keeping only articles with the most dramatic headlines", "Assuming publication date equals the date of the event"],
  "AB", "Syndication creates duplicates and copyright limits reuse; event dates often differ from publication.")
q("logs", "Web server logs recording every page request are an example of:",
  ["Event data", "Survey data", "Experimental data", "Reference data"],
  "A", "Logs are high-volume, semi-structured event data, useful for usage analysis and monitoring.")
q("reference-data", "A table of valid country codes and names used to validate other datasets is:",
  ["Reference data", "Transactional data", "Event data", "Telemetry data"],
  "A", "Reference data is a controlled list of permissible values shared across systems.")
q("master-data", "Maintaining a single trusted record of each customer or site across multiple systems is called:",
  ["Master data management", "Change data capture", "Data virtualisation", "Data lake zoning rules"],
  "A", "MDM resolves duplicates and conflicts to create a golden record.")
q("crowdsourced", "Which is a key quality risk of crowdsourced (citizen science) observations such as wildlife sightings?",
  ["Varying skill and effort among contributors", "Observations usually lack a precise location", "Data volumes are too small to analyse", "Contributors are paid per record submitted"],
  "A", "Validation, training and quality flags help; citizen science can still add great spatial coverage.")
q("data-catalogue", "A searchable inventory of an organisation's datasets with descriptions, owners and access information is a:",
  ["Data catalogue", "Data lake", "Data mart", "Data warehouse"],
  "A", "Catalogues (e.g. Microsoft Purview) improve findability and governance.")
q("special-category", "Under UK GDPR, which TWO are special category data needing extra conditions to process?",
  ["Health data", "Racial or ethnic origin", "Postcode of residence", "Job title"],
  "AB", "Special categories include health, race/ethnicity, religion, biometrics, sex life/orientation, politics and union membership.")
q("foi", "Which UK law gives the public a right to request recorded information held by public authorities?",
  ["The Freedom of Information Act 2000", "The Data Protection Act 2018", "The Digital Economy Act 2017", "The Computer Misuse Act 1990"],
  "A", "FOI covers public authority information; DPA governs personal data; the DEA enables some data sharing.")
q("data-quality-source", "A dataset downloaded from a third-party website has no documentation of how it was collected. What is the best response?",
  ["Treat it cautiously and seek provenance before relying on it", "Use it freely, as published data is usually accurate", "Combine it with other data so that any errors cancel each other out", "Delete any rows that look unusual and proceed"],
  "A", "Without provenance you cannot judge bias, coverage or quality.")
