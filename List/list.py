# myList = []

# N = int(input())

# for i in range(N):
#     command = input().split()
    
#     if command[0] == "insert":
#         myList.insert(int(command[1]), int(command[2]))
#     elif command[0] == "print":
#         print(myList)
#     elif command[0] == "remove":
#         myList.remove(int(command[1]))
#     elif command[0] == "append":
#         myList.append(int(command[1]))
#     elif command[0] == "sort":
#         myList.sort()
#     elif command[0] == "pop":
#         myList.pop()
#     elif command[0] == "reverse":
#         myList.reverse()


class ListOperations:
    def __init__(self):
        self.myList = []

    def commands(self, command):
        if command[0] == "insert":
            self.myList.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(self.myList)
        elif command[0] == "remove":
            self.myList.remove(int(command[1]))
        elif command[0] == "append":
            self.myList.append(int(command[1]))
        elif command[0] == "sort":
            self.myList.sort()
        elif command[0] == "pop":
            self.myList.pop()
        elif command[0] == "reverse":
            self.myList.reverse()

if __name__ == '__main__':
    lists = ListOperations()

    N = int(input("Enter the number of commands: "))

    for i in range(N):
        command = input("Enter command: ").split()
        lists.commands(command)
