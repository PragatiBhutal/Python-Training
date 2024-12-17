def check_weirdness(n):
    if n < 1 or n > 100:
        return "Input is out of the valid range. Please enter a value between 1 and 100."
    if n % 2 == 1:  
        return "Weird"
    elif 2 <= n <= 5:  
        return "Not Weird"
    elif 6 <= n <= 20:  
        return "Weird"
    else:  
        return "Not Weird"

if __name__ == '__main__':
    n = int(input("Enter a positive integer: ").strip())
    result = check_weirdness(n)
    print(result)
