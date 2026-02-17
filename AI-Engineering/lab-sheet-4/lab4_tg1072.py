import string

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


# 12. Write a Python program to find the median of three values.
def calculate_median(input1, input2, input3):
    list = [input1, input2, input3]
    list.sort()
    print(list[1])


calculate_median(15, 26, 29)

# 13. Write a Python program to get next day of a given date.
year = int(input("Input a year"))
month = int(input("Input a month[1-12]"))
day = int(input("Input a day [1-31]:"))


def get_next_day(year, month, day):
    days_in_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    if days_in_month.get(month) == 28:
        if day == 28:
            month += 1
            day = 1
        else:
            day += 1
    elif days_in_month.get(month) == 30:
        if day == 30:
            month += 1
            day = 1
        else:
            day += 1
    elif days_in_month.get(month) == 31:
        if day == 31:
            month += 1
            day = 1
        else:
            day += 1
    print(f"The next date is[yyyy-mm-dd] {year} {month} {day}")


get_next_day(year, month, day)


# 14. Write a Python program to create the multiplication table (from 1 to 10) of a number.
def multiplication_table(num):
    for i in range(1, 11):
        print(f"{6} x {i} = {i * 6}")


multiplication_table(6)

# 15. Write a Python program to construct the following pattern, using a nested loop number
for i in range(1, 10):
    for k in range(0, i):
        print(i)
    print("\n")

# 16. Write a programm that ask for a number to the user and clasifies it:
input = int(input("Enter number"))


def classfication():
    if input < 2:
        print("Small")
    elif input < 10:
        print("Medium")
    else:
        print("Large")


classfication()


# 17 Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
def sum(val1, val2):
    sum = val1 + val2
    if sum >= 15 and sum <= 20:
        return 20


# val1 = int(input("Enter number 1"))
# val2 = int(input("Enter number 2"))

# sum(val1, val2)


# Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a
# comma-separated sequence
def check_all_digit_even():
    for i in range(200, 240):
        orignal = i
        flag = True
        while i // 10 != 0 and flag:
            is_even_num = i % 10
            if is_even_num % 2 == 0:
                i = i // 10
            else:
                flag = False
        if flag:
            print(orignal)


check_all_digit_even()


# 19. Write a Python function to check whether a number falls in a given range.
value = int(input("Enter number"))
start = int(input("Enter start"))
end = int(input("Enter end"))
range = (start, end)


def check_that_value(range, value):
    if range[0] < value and value < range[1]:
        return True
    return False


bool_value = check_that_value(range, value)
print(bool_value)


# 21. Write a Python function that checks whether a passed string is palindrome or not.
#
def check_palindrome(input):
    result = ""
    for ch in range(len(input) - 1, -1, -1):
        result += input[ch]
    return input == result


usr_input = input("enter word")
palindrome = check_palindrome(usr_input)
print(palindrome)


# 22. Write a Python function to check whether a string is a pangram or not.
input_pangram = input("enter sentence")
letters = string.ascii_letters


def isPangram(usr_input):
    letters_found = set()
    for ch in input_pangram:
        if ch in letters:
            letters_found.add(ch)
    print(letters_found)
    return len(letters_found) == 26


isTrue = isPangram(input_pangram)
print(isTrue)


# 25
def reverse(input):
    result = ""
    for ch in range(len(input) - 1, -1, -1):
        result += input[ch]
    print(result)


user_in = input("user input")
reverse(user_in)
