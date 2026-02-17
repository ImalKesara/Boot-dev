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
