class Author:
    def __init__(self, author_name=None):
        self.author_name = author_name
        self.books = {}

    def addBook(self, title, genre):
        if self.author_name is None:
            print("A book can not be added without author name")
        else:
            if genre not in self.books:
                self.books[genre] = []
            self.books[genre].append(title)

    def setName(self, author_name):
        self.author_name = author_name

    def printDetail(self):
        if self.author_name is None:
            print("A book can not be added without author name")
        else:
            
            print("Number of Book(s):", sum(len(books) for books in self.books.values()))
            print("Author Name:", self.author_name)
            for genre, titles in self.books.items():
                print(genre + ":", ", ".join(titles))
           

# Do not change the following lines of code.
a1 = Author()
print("==========================")
a1.addBook("Ice", "Science Fiction")
print("==========================")
a1.setName("Anna Kavan")
a1.addBook("Ice", "Science Fiction")
a1.printDetail()
print("==========================")
a2 = Author("Humayun Ahmed")
a2.addBook("Onnobhubon", "Science Fiction")
a2.addBook("Megher Upor Bari", "Horror")
print("==========================")
a2.printDetail()
a2.addBook("Ireena", "Science Fiction")
print("==========================")
a2.printDetail()
print("==========================")
