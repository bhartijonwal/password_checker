# 🔐 Password Strength Checker (Python)

A Python-based tool that evaluates the strength of a password based on commonly accepted security rules such as length, uppercase and lowercase letters, digits, and special characters.

This project demonstrates basic Python programming concepts including conditional logic, string handling, and regular expressions.

---

## 📌 Features

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

---
