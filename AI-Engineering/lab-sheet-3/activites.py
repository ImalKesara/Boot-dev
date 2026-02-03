# 1. Create a tuple of at least 5 subjects and print them using a loop.
subjects = ("Maths", "Science", "English", "History", "ICT")
for subject in subjects:
    print(subject)
# 2. Create two sets of numbers and perform all set operations.
set_one = {1, 2, 4, 5}
set_two = {5, 3, 2, 1, 10, 9, 11}

print("Union:", set_one | set_two)
print("Intersection:", set_one & set_two)
print("Difference:", set_one - set_two)
print("Symmentric Difference:", set_one ^ set_two)

# 3. Create a dictionary to store student details and update/remove values.

address = {"city": "new york", "state": "texas"}

student = {"name": "kamal", "age": 23, "department": "ICT", "address": address}

student.update({"name": "Suraj"})
print(student)
student.pop("name")
print(student)

# 4. Create a nested dictionary to represent a student and their marks.
marks = {"maths": 54, "science": 89, "ict": 65, "sinhala": 45}
student.update({"marks": marks})
print(student)


# 5. Write a program to convert a tuple into a list, modify one element, and convert it back
# into a tuple.
#
tuple = ("apple", "banans", 1, 2, 4, 5)
y[1] = list()
