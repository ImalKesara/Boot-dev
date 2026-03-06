class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"{self.title} {self.price} {self.author}")


jack = Book("the dark wolf", "jack carr", 99.99)
jack.display_info()

lee = Book("The Reacher", "lee child", 99.99)
lee.display_info()
