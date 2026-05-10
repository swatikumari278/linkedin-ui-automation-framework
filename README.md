# LinkedIn Selenium Automation Framework

A clean, production-ready Selenium (Python) automation framework for LinkedIn — built with **Page Object Model**, **pytest**, and **Allure reporting**.

---

## Project Structure

```
selenium-linkedin-automation/
├── base/
│   └── base_page.py          # Reusable Selenium interactions
├── config/
│   └── config.ini            # Environment & timeout config (no real credentials)
├── pages/
│   └── linkedin_page.py      # LinkedIn Page Object
├── tests/
│   ├── conftest.py           # pytest fixtures (driver setup/teardown)
│   ├── test_linkedin.py      # LinkedIn test suite
│   └── post_content/
│       └── input_text.txt    # Post content read dynamically at runtime
├── utilities/
│   ├── config_reader.py      # Centralised config access
│   └── logger.py             # Framework-wide logger
├── reports/                  # Auto-generated test logs (git-ignored)
├── screenshots/              # Auto-generated on failure (git-ignored)
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Prerequisites

- Python 3.10+
- Google Chrome (latest)
- Selenium 4.x — **no manual chromedriver download needed** (Selenium Manager handles it)

---

## Setup

```bash
# 1. Clone the repo
git clone https://github.com/swatikumari278/selenium-linkedin-automation.git
cd selenium-linkedin-automation

# 2. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure credentials
#    Edit config/config.ini and set your LinkedIn email and password.
#    NEVER commit real credentials — use a local override file instead.
```

---

## Credentials Setup

Update `config/config.ini`:

```ini
[credentials]
linkedin_email    = your_email@example.com
linkedin_password = your_password
```

> **Security note:** `config/config.local.ini` is git-ignored. You can keep your real credentials there and point `config_reader.py` to it for local runs.

---

## Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run a specific test file
pytest tests/test_linkedin.py

# Run with Allure reporting
pytest --alluredir=allure-results
allure serve allure-results
```

---

## Test Coverage

| Test Class              | What it covers                              |
|-------------------------|---------------------------------------------|
| `TestLinkedInSignIn`    | Sign-in flow with valid credentials         |
| `TestLinkedInPostCreation` | Create a text post from an external file |

---

## Framework Design Decisions

- **Page Object Model** — All locators and interactions are encapsulated in page classes. Tests contain only assertions and flow logic.
- **Selenium Manager** — No hardcoded chromedriver path. Selenium 4.x automatically downloads and manages the correct driver.
- **Config-driven** — Base URL, timeouts, and credentials are all read from `config.ini`. No magic strings in tests.
- **Centralised logging** — All framework activity is logged to `reports/automation.log` with timestamps.
- **Fixture-based teardown** — `conftest.py` ensures the browser is always closed cleanly, even on test failure.

---

## Allure Report Example

After running with `--alluredir`, the Allure report shows:
- Test results per class
- Execution timeline
- Failure screenshots (when configured)
- Step-level breakdown

> Note: This project demonstrates Selenium + Python framework architecture using Page Object Model.  
> Some LinkedIn locators may require updates because LinkedIn UI changes frequently.


##Author

**Swati Kumari** — QA Automation Lead | Senior SDET  
[LinkedIn](https://linkedin.com/in/swati-kumari-76a028103) · [GitHub](https://github.com/swatikumari278)
