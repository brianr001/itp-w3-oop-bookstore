class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.booklist = []
    
    
    def add_book(self, book):
        self.booklist.append(book)
        
    
    def get_books(self):
        return self.booklist
        
    
    def search_books(self, title=None, author=None):
        results = []
        
        for books in self.booklist:
            
            if title:
                if title.lower() in books.title.lower():
                    results.append(books)
            
            if author:
                if books.author == author:
                    results.append(books)
        
        return results
            

# author works

class Author(object):
    
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.booklist = []
        
    def add_book(self, book):
        self.booklist.append(book)
        
    def get_books(self):
        return self.booklist

# book works

class Book(object):
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
        self.author.add_book(self)
