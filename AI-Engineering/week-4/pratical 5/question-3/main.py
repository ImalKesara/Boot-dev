with open("content.txt", "r") as file:
    print(file.read(20))
    print("Pointer position", file.tell())
    file.seek(0)
    print("After seek show pointer position", file.tell())
    print(file.readline())
    print("---------------------------")
    print(file.readlines())
