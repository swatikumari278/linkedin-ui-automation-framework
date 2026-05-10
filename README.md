
# LinkedIn UI Automation Framework

A scalable UI automation framework built using Selenium WebDriver, Python, pytest, and Page Object Model (POM) architecture.

This project demonstrates reusable automation design practices for LinkedIn workflows including login functionality, navigation validation, and maintainable Selenium framework structure.

> Note: LinkedIn UI changes frequently. Some locators may require updates over time.

---

# Tech Stack

- Python
- Selenium WebDriver
- pytest
- Page Object Model (POM)
- WebDriver Manager

---

# Framework Features

- Reusable Page Object Model architecture
- Centralized BasePage utilities
- Config-driven test execution
- Scalable test structure
- Explicit wait handling
- Reusable Selenium wrappers
- Clean separation of pages, tests, and utilities
- Pytest fixture support

---

# Project Structure

linkedin-ui-automation-framework/
│
├── base/
│   ├── base_page.py
│   └── driver_factory.py
│
├── config/
│   └── config.ini
│
├── pages/
│   └── linkedin_page.py
│
├── tests/
│   ├── conftest.py
│   └── test_linkedin.py
│
├── utilities/
│   ├── config_reader.py
│   └── custom_logger.py
│
├── requirements.txt
├── pytest.ini
├── README.md
└── .gitignore


---

# Supported Workflows

* LinkedIn login automation
* Feed navigation validation
* Reusable page interaction methods
* Config-driven credentials handling

---

# Installation

Clone repository:
git clone https://github.com/swatikumari278/linkedin-ui-automation-framework.git
Navigate to project folder:
cd linkedin-ui-automation-framework
Install dependencies:
pip install -r requirements.txt




# Configuration

Update credentials inside:
config/config.ini
Example:
linkedin_email = YOUR_EMAIL
linkedin_password = YOUR_PASSWORD


# Run Tests
Run all tests:

pytest
Run with verbose output:
pytest -v
Run specific test:

pytest tests/test_linkedin.py

# Framework Highlights

* Demonstrates scalable Selenium framework design using Python
* Uses reusable BasePage abstraction methods
* Follows Page Object Model best practices
* Designed for maintainability and readability

---

# Future Enhancements

* Allure reporting integration
* CI/CD execution with GitHub Actions
* Parallel execution support
* Docker integration
* Cross-browser execution

---

# Author

Swati Kumari
QA Automation Lead | Senior SDET
Open to QA Automation opportunities across Europe

```
```
