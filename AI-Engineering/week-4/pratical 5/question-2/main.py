with open("students.txt", "w") as file:
    names = [input("Enter student name: ") for i in range(3)]
    for name in names:
        file.write(name + "\n")

with open("students.txt", "a") as file:
    new_name = [input("Enter another student name to append: ")
                for i in range(2)]
    for name in new_name:
        file.write(name + "\n")


with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())
