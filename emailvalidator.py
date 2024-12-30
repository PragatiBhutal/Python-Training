import re

class EmailValidator:
    def is_valid(self, email):
        pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            if not (email.startswith('.') or email.endswith('.')):
                return True
        return False

if __name__ == "__main__":
    email = input("Enter an email address : ").strip()
    
    validator = EmailValidator()
    
    if validator.is_valid(email):
        print("Valid")
    else:
        print("Invalid")
