from ._helpers import make_builder

q, QUESTIONS = make_builder("4.5", "Development standards, including programming practice, testing and source control", start=101)

q("git-status", "Which command shows which files are modified, staged or untracked?",
  ["git status", "git log --oneline", "git diff --staged only", "git remote -v"],
  "A", "`git status` summarises the working tree and staging area; `git log` shows history.")
q("git-diff", "Which command shows line-by-line changes not yet staged?",
  ["git diff", "git status", "git show HEAD", "git blame"],
  "A", "`git diff` compares the working tree with the index; `git diff --staged` compares the index with the last commit.")
q("git-stash", "You need to switch branches urgently but have unfinished changes you don't want to commit. Which command helps?",
  ["git stash", "git reset --hard", "git clean -fd", "git revert HEAD"],
  "A", "Stash shelves changes so you can reapply them later; reset --hard and clean discard work.")
q("rebase-merge", "What is a key difference between `git merge` and `git rebase` when integrating main into a feature branch?",
  ["Rebase replays commits onto main; merge adds a merge commit", "Merge replays commits onto main; rebase adds a merge commit", "Rebase deletes the feature branch; merge keeps it", "Merge works locally; rebase works on the remote"],
  "A", "Rebase gives linear history but rewrites commits, so avoid rebasing branches others share.")
q("commit-messages", "Which TWO make a good commit message?",
  ["A short imperative summary, e.g. 'Fix null handling'", "A body explaining why the change was made", "A single word such as 'update' on every commit", "A full list of every file name that was changed"],
  "AB", "Git already records which files changed; the message should explain what and why.")
q("small-commits", "Why are small, focused commits preferred to one large commit at the end of the week?",
  ["They are easier to review, revert and understand", "They make the repository take up less disk space", "They prevent merge conflicts from ever happening", "They remove the need to write commit messages"],
  "A", "Atomic commits make history useful and problems easier to isolate.")
q("branch-protection", "Why protect the main branch so changes must go through a reviewed pull request with passing checks?",
  ["To stop unreviewed or failing code reaching main", "To stop anyone from reading the repository code", "To make Git store files in a compressed format", "To avoid needing any tests on feature branches"],
  "A", "Branch protection enforces the team's quality gates.")
q("large-files", "Large model files and datasets bloat a Git repository. Which TWO approaches are better?",
  ["Store them in object storage or a model registry", "Track them with Git LFS or a tool such as DVC", "Commit them weekly in a separate folder in the repository", "Email them to the team instead of storing them centrally"],
  "AB", "Git is designed for text; large binaries belong in LFS, DVC or external storage with versioning.")
q("assertions", "In pytest, what happens when an `assert` statement in a test evaluates to False?",
  ["The test is reported as failed", "The test is skipped silently", "The test is retried automatically", "The test passes with a warning"],
  "A", "pytest rewrites asserts to give detailed failure messages.")
q("fixtures", "In pytest, a fixture is mainly used to:",
  ["Provide reusable setup such as test data or connections", "Mark a test as expected to fail on some systems", "Measure how much code the tests execute", "Run the same test across several Python versions"],
  "A", "Fixtures supply and clean up test dependencies; xfail, coverage and tox cover the others.")
q("parametrise", "`@pytest.mark.parametrize` is used to:",
  ["Run one test function with several input–output cases", "Run tests in parallel across several CPU cores", "Skip tests when a parameter is not supplied", "Generate documentation from the test docstrings"],
  "A", "Parametrisation avoids copy-pasted tests for each case.")
q("edge-cases", "Which TWO are good edge cases to test for a function that computes the mean of a column?",
  ["An empty column", "A column containing missing values", "A column of ordinary positive numbers only", "A column whose name is in lower case"],
  "AB", "Edge cases probe boundaries and unusual inputs where bugs hide.")
q("property-testing", "Property-based testing (e.g. with Hypothesis) works by:",
  ["Generating many random inputs and checking a general rule holds", "Testing each class property's getter and setter methods", "Comparing outputs with a saved file from a previous run", "Measuring how long each function takes to execute"],
  "A", "e.g. 'sorting twice equals sorting once' checked across hundreds of generated inputs.")
q("snapshot-testing", "Comparing a pipeline's output against a previously approved 'golden' output file is called:",
  ["Snapshot testing", "Mutation testing", "Load testing", "Fuzz testing"],
  "A", "Useful for complex outputs; changes must be reviewed before updating the snapshot.")
q("pre-commit", "Pre-commit hooks are used to:",
  ["Run checks such as formatting and linting before a commit is made", "Deploy code to production before tests have finished running", "Merge feature branches into main automatically each night", "Back up the repository to a second remote after each push"],
  "A", "Hooks catch issues locally before they reach review or CI.")
q("github-actions", "A YAML file in `.github/workflows/` that runs tests on every pull request defines:",
  ["A GitHub Actions CI workflow", "A Docker image for production", "A Python package dependency list", "A branch protection rule"],
  "A", "GitHub Actions runs workflows on events such as push or pull_request.")
q("packaging", "Which file is the modern standard for declaring a Python project's metadata, dependencies and build system?",
  ["pyproject.toml", "setup.cfg.json", "requirements.lock.py", "package.json"],
  "A", "pyproject.toml (PEP 518/621) is the standard; package.json is for Node.js.")
q("dependency-pinning", "Why pin exact dependency versions for a deployed application?",
  ["So a later package release can't silently change behaviour", "So the application picks up the newest features automatically", "So the packages download faster from the index", "So the code works across every supported Python version"],
  "A", "Pinning (lock files) gives reproducible builds; update deliberately and test.")
q("security-deps", "Which practice helps find known vulnerabilities in a project's third-party packages?",
  ["Dependency scanning such as pip-audit", "Running the code formatter before each commit", "Increasing unit test coverage to 100%", "Renaming variables to follow PEP 8"],
  "A", "Scanners check dependencies against vulnerability databases.")
q("sql-injection", "Building a SQL query by inserting user input directly into a string risks:",
  ["SQL injection", "Data drift", "Deadlocks", "Overfitting"],
  "A", "Use parameterised queries so input is treated as data, not code.")
q("type-checking", "What does a static type checker such as mypy do?",
  ["Finds type inconsistencies by analysing code without running it", "Converts Python code into a faster compiled executable file", "Enforces types at runtime by raising errors on bad input", "Formats code so that type hints line up neatly"],
  "A", "Type hints aren't enforced at runtime; mypy checks them statically.")
q("functions-design", "Which TWO are signs a function should be refactored?",
  ["It is hundreds of lines long and does several unrelated things", "It depends on global variables that other code modifies", "It has a clear, descriptive name and a single responsibility", "It has a docstring explaining its inputs, and type hints"],
  "AB", "Long, multi-purpose functions and hidden global state make code hard to test and change.")
q("config", "Where should environment-specific settings such as database hostnames usually live?",
  ["In configuration or environment variables, outside the code", "Hard-coded as constants at the top of every module", "In comments next to the lines of code that use them", "In the commit messages for each deployment"],
  "A", "Separating config from code lets the same code run in dev, test and production.")
q("code-review-focus", "Which TWO should a reviewer of a data pipeline pull request prioritise?",
  ["Correctness of the logic and handling of edge cases", "Whether tests cover the change adequately", "Personal preference for variable naming style", "Whether the author used their favourite editor"],
  "AB", "Reviews should focus on correctness, risk and maintainability; style is best automated.")
q("readme", "Which information is most important in a project README?",
  ["What it does, how to install it and how to run it", "The personal biographies of all the contributors", "The full source code copied into one long block", "A list of every commit made to the repository"],
  "A", "A README helps newcomers get started quickly.")
q("licence", "Why should a public code repository include a licence file?",
  ["Without one, others have no clear legal right to reuse it", "Git refuses to push public repositories that lack a licence file", "It makes the repository appear higher in search results", "It encrypts the code so only licensed users can read it"],
  "A", "Default copyright applies without a licence; public sector code often uses MIT or OGL.")
q("pair-programming", "Two developers working at one computer, one writing code and one reviewing in real time, is called:",
  ["Pair programming", "Mob testing sessions", "Rubber ducking", "Trunk merging"],
  "A", "Pairing spreads knowledge and catches issues early.")
q("definition-of-done", "In Agile, a team's 'Definition of Done' is:",
  ["Shared criteria a piece of work must meet to count as complete", "The date by which the whole project must be delivered to users", "A list of features to be dropped if time runs short", "The sign-off document that ends the project contract"],
  "A", "e.g. code reviewed, tests passing, documentation updated, deployed to test.")
q("kanban-scrum", "Which TWO statements about Scrum and Kanban are true?",
  ["Scrum works in fixed-length sprints", "Kanban limits work in progress on a board", "Kanban requires two-week sprints", "Scrum forbids any visual task board"],
  "AB", "Scrum uses timeboxed sprints; Kanban uses continuous flow with WIP limits.")
