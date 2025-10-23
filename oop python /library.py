class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def display_books(self):
        print(f"\nBooks in {self.name}:")
        if not self.books:
            print("No books in the library.")
        for book in self.books:
            book.display_info()
