class InputValidator:
    def validate_age(self, input_value):
        if input_value.isdigit() and int(input_value) > 0:
            return True
        return False

if __name__ == "__main__":
    validator = InputValidator()
    
    while True:
        age = input("Enter your age: ").strip()
        if validator.validate_age(age):
            print(f"Your age is {age}.")
            break
        else:
            print("Invalid input. Please enter a positive number.")
