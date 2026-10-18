from ._helpers import make_builder

q, QUESTIONS = make_builder("4.5", "Development standards, including programming practice, testing and source control")

# --- Source control -----------------------------------------------------------------
q("git-basics", "What does `git commit` do?",
  ["Sends local commits to the remote repository", "Records staged changes as a snapshot in local history", "Downloads new commits from the remote without merging", "Adds changed files to the staging area"],
  "B", "Commits are local. `git push` sends them, `git fetch` downloads without merging, `git add` stages.")
q("git-basics", "What does `git pull` do?",
  ["Fetches remote changes and merges them into the current branch", "Fetches remote changes without changing the working branch", "Sends local commits on the current branch to the remote", "Creates a copy of the remote repository on the local machine"],
  "A", "`git pull` = `git fetch` followed by a merge (or rebase if configured). The others are fetch, push and clone.")
q("git-staging", "Which command stages changes to be included in the next commit?",
  ["git add", "git stash", "git commit", "git checkout"],
  "A", "`git add` moves changes to the staging area; `git stash` shelves them temporarily.")
q("branching", "Why do teams develop new features on separate branches?",
  ["To keep the main branch stable until changes are reviewed and merged", "To keep a separate copy of the code for each deployment environment", "To store large data files outside the main repository history", "To avoid having to resolve conflicts when changes are combined"],
  "A", "Feature branches support parallel work and code review via pull requests; conflicts can still occur on merge.")
q("pull-requests", "Which TWO are benefits of code review via pull requests?",
  ["Catching bugs and design issues before merging", "Sharing knowledge of the code across the team", "Replacing the need for automated test suites", "Shortening the time from commit to deployment"],
  "AB", "Reviews improve quality and spread understanding but do not replace testing, and they add some delay.")
q("merge-conflict", "A merge conflict occurs when:",
  ["Two branches change the same lines in different ways", "A branch is merged before its tests have passed", "Two developers commit to the same branch on the same day", "A file is renamed on one branch and left unchanged on another"],
  "A", "Git can't decide which change to keep, so the conflict must be resolved manually. Same-day commits and simple renames usually merge cleanly.")
q("revert-reset", "A bad commit has already been pushed to a shared branch. What is the safest way to undo it?",
  ["Use `git revert` to add a commit that reverses it", "Use `git reset --hard` and force-push the branch", "Use `git commit --amend` and push the amended commit", "Use `git checkout` to switch back to the previous commit"],
  "A", "Revert preserves history; reset/amend with force-push rewrites shared history and disrupts collaborators.")
q("secrets", "An API key is needed by a script stored in Git. What is best practice?",
  ["Commit it in a separate config file kept in a private repository", "Load it from an environment variable or secrets manager at runtime", "Encode it in base64 within the script so it is not readable", "Commit it, then delete it in the next commit once deployed"],
  "B", "Use environment variables or a vault (e.g. Azure Key Vault). Base64 is not encryption, private repos leak, and deleted secrets remain in history.")
q("gitignore", "Which TWO items should typically be listed in a project's .gitignore?",
  ["Virtual environment and cache folders", "Local files containing credentials", "The requirements.txt lock file", "Unit tests and test fixtures"],
  "AB", "Ignore generated artefacts and secrets; commit source, tests and dependency files.")
q("semver", "Under semantic versioning (MAJOR.MINOR.PATCH), a release that introduces a backwards-incompatible API change should increment:",
  ["PATCH", "MINOR", "MAJOR", "MINOR and PATCH"],
  "C", "MAJOR for breaking changes, MINOR for backwards-compatible features, PATCH for bug fixes.")

# --- Testing ------------------------------------------------------------------------
q("test-types", "A test that checks a single function in isolation, e.g. that `clean_postcode(' bs1 4xe ')` returns 'BS1 4XE', is:",
  ["A unit test", "An integration test", "A smoke test", "A system test"],
  "A", "Unit tests verify small units of code in isolation.")
q("test-types", "A test that runs the pipeline end-to-end against a test database to check that components work together is:",
  ["A unit test", "An integration test", "A static analysis check", "A property-based test"],
  "B", "Integration tests check interactions between components.")
q("test-types", "Re-running existing tests after a change to confirm previously working behaviour still works is called:",
  ["Regression testing", "Exploratory testing", "Smoke testing", "Mutation testing"],
  "A", "Regression tests guard against reintroducing bugs. Smoke tests are quick checks that the basics work.")
q("uat", "User acceptance testing (UAT) is primarily concerned with:",
  ["Whether it meets business needs from the user's view", "Whether each function returns the expected output", "Whether the system performs well under realistic peak load", "Whether the code follows the team's style guide"],
  "A", "UAT is performed by or with end users before sign-off.")
q("tdd", "In test-driven development (TDD), what is the usual cycle?",
  ["Write the code, then write tests to cover it, then refactor", "Write a failing test, make it pass, then refactor", "Write all the tests for a feature, then write all the code", "Refactor the code, then add tests, then add new features"],
  "B", "TDD is red–green–refactor in small increments.")
q("mocking", "Why would you mock an external API in a unit test?",
  ["To make the test fast, repeatable and independent of the network", "To check that the real API still returns the expected schema", "To measure the API's response time under a realistic production load", "To increase the test coverage reported for the API client"],
  "A", "Mocks replace dependencies with controlled fakes. Checking the real API's behaviour is a contract/integration test.")
q("coverage", "A project reports 95% test coverage. Which statement is true?",
  ["95% of the code's behaviour has been verified as correct", "95% of lines ran during tests, but the checks may be weak", "95% of the tests passed on the most recent CI run", "95% of user-facing features have acceptance tests"],
  "B", "Coverage measures execution, not the quality of assertions.")
q("data-testing", "Which TWO are useful automated tests for a data pipeline?",
  ["Schema checks that expected columns and types exist", "Assertions on value ranges and null rates", "Manual review of a sample of rows each run", "Comparing run time with the previous run"],
  "AB", "Data validation tests (e.g. with Great Expectations or pandera) catch upstream data issues early. Manual review isn't automated; run time is monitoring, not correctness.")

# --- CI/CD & environments -------------------------------------------------------------
q("ci-cd", "Continuous Integration (CI) means:",
  ["Automatically building and testing code on each push or merge", "Automatically releasing every change to production users", "Merging all developers' branches together at the end of each sprint", "Integrating data from multiple sources into one warehouse"],
  "A", "CI catches integration problems early; continuous delivery/deployment automates release.")
q("reproducibility-env", "Which TWO practices help ensure a Python analysis can be reproduced on another machine?",
  ["A virtual environment with pinned dependency versions", "Setting random seeds where randomness is used", "Installing the latest version of each package", "Saving notebook outputs instead of the code"],
  "AB", "Pinned environments and fixed seeds make results repeatable; 'latest' versions change over time.")
q("docker", "What problem does containerising an application with Docker mainly solve?",
  ["Inconsistent environments between development and deployment", "Tracking changes to code made by different developers", "Scaling a database across several physical servers in a cluster", "Scheduling pipeline tasks in the right order"],
  "A", "Containers package code with its dependencies and runtime. The others are solved by version control, distributed databases and orchestrators.")
q("notebooks", "What is a known risk of relying on Jupyter notebooks for production code?",
  ["Hidden state and out-of-order execution hurt reproducibility", "They are unable to import third-party Python packages", "They run code noticeably more slowly than an equivalent .py script", "They store outputs in a format Git is unable to track"],
  "A", "Refactor stable logic into tested modules; keep notebooks for exploration and reporting. Notebooks are JSON, which Git tracks (if noisily).")

# --- Programming practice ----------------------------------------------------------
q("pep8", "PEP 8 is:",
  ["Python's style guide", "Python's testing framework", "Python's type-hint standard", "Python's packaging format"],
  "A", "PEP 8 covers style; type hints are PEP 484. Tools such as Black and Ruff help enforce style.")
q("linting", "Which TWO tools automatically improve code consistency and catch common errors?",
  ["Linters such as Ruff or Flake8", "Formatters such as Black", "Profilers such as cProfile", "Debuggers such as pdb"],
  "AB", "Linters flag issues and formatters enforce style automatically; profilers and debuggers are interactive diagnostic tools.")
q("dry", "The DRY principle means:",
  ["Factor repeated logic into reusable functions or modules", "Keep each function short and focused on a single task", "Remove code that is no longer called by the application", "Write the simplest code that meets current requirements"],
  "A", "Don't Repeat Yourself. The others are single responsibility, dead-code removal and YAGNI/KISS.")
q("docstrings", "Which TWO practices make functions easier for others to understand and use correctly?",
  ["Docstrings describing purpose, parameters and returns", "Type hints on parameters and return values", "Global variables shared between related functions", "Short abbreviated names to keep lines compact"],
  "AB", "Documentation and type hints communicate intent and enable static checking.")
q("exceptions", "Which is better practice for error handling in Python?",
  ["A bare `except:` that logs the error and continues", "Catching specific exceptions and handling them meaningfully", "Wrapping the whole script in a single try/except block so the run can complete", "Returning None from functions instead of raising errors"],
  "B", "Broad catches hide bugs; specific handling makes failures visible and recoverable.")
q("logging", "Why use Python's `logging` module rather than `print` in a production pipeline?",
  ["It supports levels, timestamps and routing to files or monitoring", "It makes the pipeline run faster by buffering output", "It automatically stops sensitive values from appearing in the output", "It is required for code to run under a scheduler"],
  "A", "Structured logs are essential for monitoring and debugging production systems; they don't redact secrets automatically.")
q("magic-numbers", "A function contains `if score > 0.73:` with no explanation. What is the recommended improvement?",
  ["Use a named, documented constant or configuration value", "Round the value to 0.7 so it is easier to remember", "Add a comment on the line explaining where 0.73 came from", "Pass the value in as a required function argument"],
  "A", "A named constant or config value documents meaning and makes changes safe; a comment helps less as code changes.")
q("model-versioning", "Which tool is commonly used to track ML experiments, parameters, metrics and model versions?",
  ["MLflow", "Airflow", "Prometheus", "Terraform"],
  "A", "MLflow tracks experiments and models. Airflow orchestrates pipelines, Prometheus monitors metrics, Terraform provisions infrastructure.")
q("agile", "In Agile delivery, a 'user story' is typically written as:",
  ["'As a <user>, I want <goal> so that <benefit>'", "'Given <context>, when <action>, then <outcome>'", "'The system shall <function> within <time limit>'", "'If <condition> then <action>, else <alternative>'"],
  "A", "User stories capture needs from the user's perspective; Given/When/Then is the format for acceptance criteria.")
