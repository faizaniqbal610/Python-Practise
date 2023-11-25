class Library:
    def __init__(self) -> None:
        self.books = []
        self.no_of_books = 0

    def addBook(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)
    
    def showInfo(self):
        print(f"Library has {self.no_of_books} Books. And these books are")
        for book in self.books:
            print(book)


a = Library()
a.addBook("Iron man 1")
a.addBook("Iron man 2")
a.addBook("Iron man 3")
a.showInfo()

