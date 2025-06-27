# 🛒 EazyCart Automation Project (SauceDemo.com)

This is a real-time Selenium automation framework built to test core e-commerce functionalities of [SauceDemo](https://www.saucedemo.com/).  
It uses Python, PyTest, and the Page Object Model (POM) design pattern, with Excel integration for data-driven testing.

---

## 🚀 Technologies Used
- Selenium WebDriver
- Python
- PyTest
- Page Object Model (POM)
- openpyxl (Excel-based test data)
- HTML Test Reporting (`pytest-html`)
- Git & GitHub

---

## ✅ Features Automated

- Login with credentials from Excel
- Invalid login attempt handling
- Add product to cart
- Remove product from cart
- Proceed to checkout
- Enter customer information
- Complete the order
- Verify success message
- Logout functionality
- Handle alerts and dynamic waits

---

## 📁 Folder Structure



## Folder Structure
eazycart_automation/
├── testcases/
│ ├── test_login.py
│ ├── test_invalid_login.py
│ ├── test_cart_checkout.py
│ ├── test_logout.py
├── pages/
│ ├── login_page.py
│ ├── home_page.py
│ ├── cart_page.py
│ ├── checkout_page.py
├── testdata/
│ └── credentials.xlsx
├── reports/
│ └── checkout_report.html
├── conftest.py
└── README.md

---

## How to Run the Tests

  1. Clone the repository:
  ```bash
  git clone https://github.com/your-username/eazycart-automation.git
  cd eazycart-automation

  2 Install dependencies:
  pip install -r requirements.txt

  3 Run the test suite and generate an HTML report:
  pytest --html=reports/checkout_report.html

## Author
Amulya Kotte
Aspiring QA Automation Engineer
"Learning, building, and testing to make software better." 