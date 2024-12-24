class SubstringCounte:
    def __init__(self, string, sub_string):
        self.string = string
        self.sub_string = sub_string

    def count_substring(self):
        count = 0
        sub_len = len(self.sub_string)

        for i in range(len(self.string) - sub_len + 1):
            if self.string[i:i + sub_len] == self.sub_string:
                count += 1

        return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    substring_counte = SubstringCounte(string, sub_string)
    count = substring_counte.count_substring()
    print(count)
