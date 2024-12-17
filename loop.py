class SquareNumbers:
    def __init__(self, n):
        self.n = n

    def print_squares(self):
        for i in range(self.n):
            print(i * i)

if __name__ == '__main__':
    n = int(input("Enter a number :"))
    if 1 <= n <= 20:
        square_numbers = SquareNumbers(n)
        square_numbers.print_squares()
    else:
        print("Input must be between 1 and 20.")
