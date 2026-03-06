from calcualor import add, divide, multiply, subtract

try:
    num = divide(10, 0)
    print(num)
except ZeroDivisionError:
    print("Cannot divided by zero")
finally:
    print("proccess end")
