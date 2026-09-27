class Book:
    library_name = "Campus Library"
    def __init__(self, title):
        self.title = title
        self.is_read = False  

    def mark_read(self):
        self.is_read = True
print(Book.library_name)
print(Book("Done").library_name)