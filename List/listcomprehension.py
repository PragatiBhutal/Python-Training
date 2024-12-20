class ListComprehensions:
    def __init__(self, x, y, z, n):
        self.x = x
        self.y = y
        self.z = z
        self.n = n

    def coordinates(self):
        return [[i, j, k] for i in range(self.x + 1)
                           for j in range(self.y + 1)
                           for k in range(self.z + 1)
                           if i + j + k != self.n]


if __name__ == '__main__':
    x = int(input("Enter value for x: "))
    y = int(input("Enter value for y: "))
    z = int(input("Enter value for z: "))
    n = int(input("Enter value for n: "))
    
    comprehension = ListComprehensions(x, y, z, n)
    result = comprehension.coordinates()
    print(result)
