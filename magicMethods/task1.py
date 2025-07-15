class Book():
    def __init__(self, name, author, page):
        self.name = name
        self.author = author
        self.page = page
    
    def __str__(self):
        return (f"{self.name},{self.author}, {self.page}")
    
    def __eq__(self, value):
        return self.name == value.name and self.author == value.author and self.page == value.page


book1 = Book("Harry Potter", "J.K. Rowling", 500)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 300)
book3 = Book("Harry Potter", "J.K. Rowling", 500)

for i in [book1, book2, book3]:
    print(i)
    
print(book1 == book3)