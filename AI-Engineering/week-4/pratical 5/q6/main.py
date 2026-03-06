while True:
    try:
        value = int(input("enter an integer"))
        break
    except ValueError:
        print("Ops wrong value enter an integer value")
