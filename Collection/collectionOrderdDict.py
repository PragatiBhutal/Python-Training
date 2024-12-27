from collections import OrderedDict

class Products:
    def __init__(self):
        self.dictionary = OrderedDict()

    def add_product(self, item_name, price):
        if item_name in self.dictionary:
            self.dictionary[item_name] += price
        else:
            self.dictionary[item_name] = price

    def display_products(self):
        print("\nItems and net prices:")
        for item, price in self.dictionary.items():
            print(item, price)

def main():
    n = int(input("Enter the number of items: "))
    products = Products()

    for i in range(n):
        input_line = input("Enter item name and price: ")
        parts = input_line.split()
        item_name = " ".join(parts[:-1])
        price = int(parts[-1])

        products.add_product(item_name, price)

    products.display_products()

if __name__ == "__main__":
    main()
