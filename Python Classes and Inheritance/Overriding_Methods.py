#If a method is defined for a class, and also defined for its parent class, the subclass’ method is called and not the parent’s.


class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return("'{}' by {}".format(self.title, self.author))


class PaperBook(Book):
    def __init__(self, title, author, pages):
        Book.__init__(self, title, author)
        self.pages = pages
        

class EBook(Book):
    def __init__(self, title, author, size):
        Book.__init__(self, title, author)
        self.size = size
                
    
    
myEBook = EBook('The Odissey', 'Homer', 2)
myPaperBook = PaperBook('The Odissay', 'Homer', 500)
print(myEBook.size)
print(myPaperBook.pages)


#let's say we want to create a new class called Library, that takes counts of all EBooks and PaperBooks

class Library:
    def __init__(self):
        self.books = []
        
    def addBook(self, book):
        self.books.append(book)
        
    def getNumBooks(self):
        return(len(self.books))
    
    def __str__(self):
        return("There are {} books in the library".format(len(self.books)))
    
    

new_library = Library()

new_library.addBook(myEBook)
new_library.addBook(myPaperBook)

print(new_library.getNumBooks())
print(new_library)       
        