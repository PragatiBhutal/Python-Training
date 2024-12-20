class StringExample:
    def __init__(self, line):
        self.line = line

    def split_and_join(self):
        words = self.line.split(" ")
        result = "-".join(words)
        return result

if __name__ == '__main__':
    line = input("Enter a sentence: ")
    example = StringExample(line)
    result = example.split_and_join()
    print(result)
