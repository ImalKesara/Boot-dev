class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"name {self.name} age {self.age}")


class Student(Person):
    def __init__(self, name, age, stu_id, grade):
        super().__init__(name, age)
        self.stu_id = stu_id
        self.grade = grade

    def display_student(self):
        print(f"{self.stu_id} {self.grade} | {self.name} {self.age}")


sasanka = Student("Kamal", 89, 1001, "Grade 11")
sasanka.display_student()
