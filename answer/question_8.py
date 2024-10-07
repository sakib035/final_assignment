# Suggested code may be subject to a license. Learn more: ~LicenseLog:1479734646.
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def get_description(self):
        return f"{self.title} by {self.author}, Pages: {self.pages}"


my_book = Book("Himu", "Humayun Ahmed", 200)

print(my_book.get_description())