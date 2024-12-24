class StringMutator:
    def __init__(self, string):
        self.string = string

    def mutate(self, position, character):
        self.string = self.string[:position] + character + self.string[position + 1:]

    def get_string(self):
        return self.string

if __name__ == '__main__':
    s = input("Enter the string: ")
    
    string_mutator = StringMutator(s)

    i, c = input("Enter the position and character (separated by space): ").split()

    string_mutator.mutate(int(i), c)

    print(string_mutator.get_string())
