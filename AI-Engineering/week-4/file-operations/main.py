from mymath import add, subtract

# step 1: create a file and write some content to it

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

print("--------------------------------------------------")

# step 2: using (with Statement) you dont need to close the file, it will automatically close after the block of code is executed
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

print("================================================")

# file methods pratice
with open("sample.txt", "r") as file:
    print(file.read(5))  # read first 10 characters
    # get the current position of the pointer(it will be 10 mostly end)
    print("Pointer position:", file.tell())
    # move the pointer to the beginning of the file (first character)
    file.seek(0)
    # get the current position of the pointer(it will be 0)
    print("After seek pointer position:", file.tell())
    print("First line:", file.readline())

print("================================================")

# writing (overwrite) to a file
with open("sample.txt", "w") as file:
    file.write("write this new line to the file\n")
    file.write("python is great for file operations\n")
    print("File has been overwritten with new content")


with open("sample.txt", "a") as file:
    file.write("this line will be appended to the file\n")
    print("New line has been appended to the file")


print("================================================")

# Part 2 handling exceptions while working with files
try:
    num = int(input("Enter a number:"))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Invalid input, please enter a number")
finally:
    print("Program completed")


print("================================================")


# step custom exception
# inherit from the base Exception class
class NegativeNumberError(Exception):
    pass


try:
    number = int(input("Enter a positive number: "))
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed")
except NegativeNumberError as e:
    print("Error:", e)

print("================================================")

print(add(5, 3))
print(subtract(5, 3))

print("================================================")


# Part 4 object oriented programming
class Student:
    # self is a reference to the current instance of the class, it is used to access the attributes and methods of the class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Teacher:
    #  default constructor
    def __init__(self):
        pass

    def display_info(self):
        print(f"Name: {self.name}, Subject: {self.subject}")


s1 = Student("Gomez", 20)
s1.display_info()

print("================================================")

# step 9 inheritance


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def study(self):
        print(f"{self.name} is studying and his age is {self.age}")


s2 = Student("Morticia", 22)
s2.display_info()
s2.study()

print("================================================")


class bankAccount:
    def __init__(self):
        self.__balance = 0  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = bankAccount()
account.deposit(5000)
print("Balance:", account.get_balance())

print("================================================")


class Animal:
    def __init__(self):
        print("parent  constructor called")

    def make_sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def make_sound(self):
        print("Dog barks")


class Cat(Animal):
    def make_sound(self):
        print("Cat meows")


animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()
