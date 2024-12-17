class Consecutive:
    def consecutive_numbers(self,n):
        if 1 <= n <= 150:
            for i in range(1, n + 1):
                print(i, end="")
        else:
            print("Input out of range")

if __name__ == "__main__":
    n = int(input("Enter The Input Here :"))
    consecutive = Consecutive()
    result = consecutive.consecutive_numbers(n)