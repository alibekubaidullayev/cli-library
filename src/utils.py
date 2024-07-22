import time
from typing import Union

from models import Book
from screen import Screen
from menu import Menu


def accept_input(instance: object, field_name: str) -> Union[bool, str]:
    if not hasattr(instance, field_name):
        raise AttributeError(f"{instance} has no attribute {field_name}")

    attribute_type = type(getattr(instance, field_name))

    inp: str = input(f"Insert {field_name} ('X' to quit assignment)")

    if inp.lower() == "x":
        return False

    try:
        casted_inp = attribute_type(inp)
    except ValueError:
        return f"Error casting input to {attribute_type.__name__}. Please, try again!"

    try:
        setattr(instance, field_name, casted_inp)
    except AttributeError as e:
        return f"Error setting attribute: {e}. Please, try again!"

    return True


def book_inserter(book: Book, attr: str) -> None:
    while True:
        result: Union[bool, str] = accept_input(book, attr)
        if result is True:
            print("Accepted!")
            time.sleep(0.3)
            break
        if result is False:
            print("'X' was pressed. Leaving book adding menu...")
            time.sleep(1)
            break

        print(result)


class BookCreationContext:
    def __init__(self):
        self.book = Book()

    def is_ready_to_confirm(self):
        return self.book.author and self.book.title and self.book.year

    def reset(self):
        self.__init__()


def _add_book_setup(context: BookCreationContext) -> Menu:
    book_creation_menu = Menu("Add book")
    book_creation_menu.add_element(
        "Title", lambda: book_inserter(context.book, "title")
    )
    book_creation_menu.add_element(
        "Author", lambda: book_inserter(context.book, "author")
    )
    book_creation_menu.add_element("Year", lambda: book_inserter(context.book, "year"))

    book_creation_menu.add_element("Confirm", lambda: print(context.book))

    return book_creation_menu


def add_book_setup(context: BookCreationContext):
    context.reset()
    print("ads")
    return _add_book_setup(context)
