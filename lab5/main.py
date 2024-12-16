class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"название книги: {self.title}, автор: {self.author}, год: {self.year}"


book = Book("Война и мир ", "Л.Н.Толстой", 1867)

print(book.get_info())
