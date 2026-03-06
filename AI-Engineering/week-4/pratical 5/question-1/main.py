file = open("country.txt", "r")
code_line = 1
for line in file:
    print(f"{code_line} : {line.strip()}")
    code_line += 1
file.close()
