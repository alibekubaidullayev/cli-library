from models import Book
from utils import accept_input


book = Book()
accept_input(book, "title")
print(book)

