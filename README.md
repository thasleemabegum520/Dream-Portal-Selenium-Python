# Dream Portal – Selenium Automation (Python)

## Overview

This project contains automated UI tests for the Dream Portal application using Selenium WebDriver with Python and pytest.

The automation follows the Page Object Model (POM) design pattern to keep page-specific locators and actions separate from test cases.

## Technologies Used

- Python
- Selenium WebDriver
- pytest
- PyCharm
- Git & GitHub

## Project Structure

```text
Dream-Portal-Selenium_Python/
├── pages/
│   ├── mydreams.py
│   ├── dreams_diary.py
│   └── dreams_total.py
│
├── tests/
│   ├── conftest.py
│   └── test_dream_portal.py
│
├── requirements.txt
└── README.md
```

## Test Coverage

The project includes automated tests for:

- Loading animation
- Main content and My Dreams button
- Dream Diary and Dream Total windows
- Number of dreams
- Dream type validation (Good/Bad)
- Validation that all table cells are populated
- Recurring dream validation
- Dream statistics validation

## Test Results

All automated test cases passed successfully.

## Design Approach

The project uses the **Page Object Model (POM)** approach.

- Page classes contain locators and page-specific methods.
- Test classes contain the test scenarios.
- `Tests/conftest.py` provides the WebDriver fixture and browser setup/teardown.
- Explicit waits are used where required.
- Python assertions are used to validate expected application behavior.

## How to Run

1. Clone the repository.
2. Open the project in PyCharm.
3. Create and activate a virtual environment.
4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Run the tests:

```bash
pytest
```

## Application

Dream Portal:

https://arjitnigam.github.io/myDreams/

## Author

**Thasleema Shaik**