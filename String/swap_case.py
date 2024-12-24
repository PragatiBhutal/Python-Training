class CaseSwapper:
    def __init__(self, string):
        self.string = string

    def swap_case(self):
        return self.string.swapcase()

if __name__ == '__main__':
    s = input("Enter the string: ")
    case_swapper = CaseSwapper(s)
    result = case_swapper.swap_case()
    print(result)
