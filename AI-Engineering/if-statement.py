number = 10
if number > 0:
    print("Number is positive")

print("-------------------------------------------------")

number = -5
if number > 0:
    print("Positive number")
else:
    print("negative number")

print("-------------------------------------------------")

number = 0
if number > 0:
    print("posi number")
elif number == 0:
    print("number is zero")
else:
    print("negative number")

print("-------------------------------------------------")


# nested if statement
number = 5
if number >= 0:
    if number == 0:
        print("number is zero")
    else:
        print("number is positive")
else:
    print("number is negative")

print("-------------------------------------------------")


# for loops
for i in range(5):
    print(i)

print("-------------------------------------------------")

languages = ["java", "C", "rust", "svelte"]
for lan in languages:
    print(lan)


print("-------------------------------------------------")

# for loops with else
#

digits = [0, 3, 4, 5]
for digit in digits:
    print(digit)
else:
    print("all the elements has been read")

print("-------------------------------------------------")

i = 1
while 5 > i:
    print(i)
    i += 1

print("-------------------------------------------------")


computer = 0
while computer < 3:
    print("inside loop")
    computer += 1
else:
    print("outside the loop")


print("-------------------------------------------------")


# infinite loop
#
while True:
    print("This loop runs forever")
    break

# continue statement

num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)


def greeting(nane, message="Hi"):
    return f"{message} , {nane}"


helo = greeting("imal")
print(helo)


# recursive functions


# A functions that calls itself
#
#
def count_down(start):
    print(start)
    next_sum = start - 1
    if next_sum > 0:
        count_down(next_sum)


count_down(3)
