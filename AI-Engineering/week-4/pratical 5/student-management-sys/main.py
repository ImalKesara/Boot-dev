# 1.Ask user to enter
# name
# marks
# 2 create a student class
# calculate_total()
# calculate_avg()

# 3.save records in a file
# 4. read records from a file and display


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_avg(self):
        return self.calculate_total() / len(self.marks)


with open("students.txt", "w") as file:
    name = input("enter name :- ")
    marks = [int(input("enter marks")) for i in range(3)]
    file.write(f"{name},{marks[0]},{marks[1]},{marks[2]}\n")


with open("students.txt", "r") as file:
    for line in file:
        data = line.split(",")
        name = data[0]
        marks = list(map(int, data[1:]))
        student = Student(name, marks)
        print(
            f"Name: {student.name} , Total : {student.calculate_total()} Avg : {student.calculate_avg()}"
        )
        for mark in marks:
            print(mark)
