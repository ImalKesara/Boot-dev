# 1. Write a program which asks the user for a number. If number is even print ‘Even’, else
# print ‘Odd’.

number = 5
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# 2. Write a program to print counting from 1 to 10.
i = 1
while i <= 10:
    print(i)
    i += 1


# 3. Write a program which prints all the divisors of a number.
number = 12
k = 1
while k < number:
    if number % k == 0:
        print(f"{k} is a divisor")
    k += 1

# 4. Write a program to check if input number is a prime number.
# 7. Write a program to calculate factorial of a number.
num = int(input("Enter a number"))
i = 1
total = 1
while i <= num:
    total = total * i
    i += 1

print(total)


# 11. Write a Python program to construct the following pattern, using a nested for loop.
for i in range(1, 6):
    print(i * " * ")
else:
    for x in range(i - 1, 0, -1):
        print(x * " * ")
