class StudentRecords:
    def __init__(self):
        self.students = []

    def add_student(self, name, score):
        self.students.append([name, score])

    def get_second_lowest_students(self):
        scores = sorted(set(score for name, score in self.students))
        second_lowest_score = scores[1]
        names = [name for name, score in self.students if score == second_lowest_score]
        return sorted(names)

if __name__ == '__main__':
    records = StudentRecords()

    n = int(input("Nmber of students: "))

    for i in range(n):
        name = input("Student name: ")
        score = float(input("Student score: "))
        records.add_student(name, score)

    second_lowest = records.get_second_lowest_students()
    for name in second_lowest:
        print(name)