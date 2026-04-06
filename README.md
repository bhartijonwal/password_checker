# 🔐 Password Strength Checker (Python)

A Python-based tool that evaluates the strength of a password based on commonly accepted security rules such as length, uppercase and lowercase letters, digits, and special characters.

## Why this project is useful
This project demonstrates:
- Input validation and string analysis.
- Rule-based security checks.
- Structured result modeling using a dataclass.
- Automated testing with `pytest`.
---

## Features

- Checks minimum password length
- Detects presence of:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Classifies passwords into:
  - Weak
  - Moderate
  - Strong
- Provides feedback to help users create stronger passwords

---

## 🛠 Technologies Used

- Python 3.14
- Regular Expressions (`re` module)

---

## ⚙️ How It Works

The program evaluates a password based on several criteria:

| Criteria | Description |
|--------|-------------|
| Length | Minimum recommended length |
| Uppercase letters | At least one capital letter |
| Lowercase letters | At least one small letter |
| Numbers | At least one digit |
| Special characters | Symbols like `! @ # $ %` |

The password is scored based on these checks and categorized accordingly.

<img width="579" height="235" alt="image" src="https://github.com/user-attachments/assets/d59c5b11-5429-4ca9-8a96-6ad68cdebb89" />

---
