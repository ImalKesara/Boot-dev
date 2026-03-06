class DivisionByZero(Exception):
    pass


try:
    numOne = int(input("Enter number one"))
    numTwo = int(input("Enter number two"))
    if numTwo == 0:
        raise DivisionByZero("Cant divided by zero")
    result = numOne / numTwo
    print(result)

except DivisionByZero as e:
    print("Error", e)
except ValueError:
    print("Please provide int values")
