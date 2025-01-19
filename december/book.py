class Publisher:
    def __init__(self, name):
        self.name = name

class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def show_Details(self):
        print(f"Publisher : {self.name}")
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")

class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def show_Details(self):
        print(f"Publisher : {self.name}")
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Price : {self.price}")
        print(f"Pages : {self.no_of_pages}")


# Taking user input
publisher_name = input("Enter the Publisher Name: ")
book_title = input("Enter the Book Title: ")
book_author = input("Enter the Book Author: ")
book_price = input("Enter the Book Price: ")
book_pages = int(input("Enter the Number of Pages: "))

# Creating an instance and showing details
b1 = Python(publisher_name, book_title, book_author, book_price, book_pages)
b1.show_Details()
