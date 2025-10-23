class Book:
    def __init__(self, title, author, isbn, available):
        self.title = title
        self.author = author
        self.__isbn = isbn   
        available = True     
        self.available = available
