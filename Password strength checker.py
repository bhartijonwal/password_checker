# Password Strength Checker

import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak password: password must be atleast 8 character long."
    
    if not any(char.isdigit() for char in password):
        return "Weak password: password must contain a digit or numerical value."
    
    if not any(char.isupper() for char in password):
        return "Weak password: password must contain an upper character."
    
    if not any (char.islower() for char in password):
        return "Weak password: password must contain an lower character."
    
    if not re.search(r'[!@#$%^&**(){}<>.?]', password):
        return "Medium password: password must contain a special character."
    
    return "Strong password: Your password is secured!"

def password_checker():
    print("Welcome to the password strength checker!")

    while True:
        password = input ("Enter your password (or type 'exit' to quit):")

        if password.lower() == 'exit':
            print("Thank you for using this tool")
            break

        result = check_password_strength(password)
        print(result)


if __name__ == "__main__":
    password_checker()