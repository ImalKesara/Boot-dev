# Assignment
# Complete the binary_string_to_int function. It takes three binary strings as input and returns each of them in the same order as integers. Each integer is the numerical value of the string when interpreted as binary.

# For example:


binary_str = "100"
num = int(binary_str, 10)
print(num)


def binary_string_to_int(num_servers, num_players, num_admins):
    num_one = int(num_servers, 2)
    num_two = int(num_players, 2)
    num_three = int(num_admins, 2)
    return num_one, num_two, num_three


data_a, data_b, data_c = binary_string_to_int("100", "101", "110")
print(data_a, data_b, data_c)
