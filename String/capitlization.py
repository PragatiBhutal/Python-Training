class NameCapitalizer:
    def __init__(self, name):
        self.name = name

    def capitalize_name(self):
        return ' '.join(word.capitalize() for word in self.name.split(' '))

if __name__ == '__main__':
    s = input("Enter the full name: ")

    capitalizer = NameCapitalizer(s)
    result = capitalizer.capitalize_name()
    print(result)
