class Shape:
    def area(self):
        print("Shape")


class Rectangle(Shape):
    def area(self):
        print("Rectangle")


class Circle(Shape):
    def area(self):
        print("Circle")


shapes = [Rectangle(), Circle()]
for shape in shapes:
    shape.area()
