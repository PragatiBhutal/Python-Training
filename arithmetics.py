def calculate_sum(a, b):
    return a + b

def calculate_difference(a, b):
    return a - b

def calculate_product(a, b):
    return a * b

def calculate_integer_division(a, b):
    return a // b

def calculate_floating_division(a, b):
    return a / b

if __name__ == '__main__':
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))
    
    print("Sum_result =", calculate_sum(a, b))
    print("Diff_Result =", calculate_difference(a, b))
    print("Product_Result =", calculate_product(a, b))
    print("Division of Integer =", calculate_integer_division(a, b))
    print("Division of Floating =", calculate_floating_division(a, b))