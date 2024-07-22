from typing import Union

from models import Book
from screen import Screen


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


def book_inserter(screen: Screen, book: Book, attr: str) -> None:
    while True:
        result: Union[bool, str] = accept_input(book, attr)
        if result is True:
            break
        if result is False:
            print("'X' was pressed. Leaving book adding menu...")
        print(result)


if __name__ == "__main__":
    book: Book = Book(author="John")
    book.year = 1984
    book2: Book = Book(title="How to become someone")
    book3: Book = Book()

    while True:
        result: Union[bool, str] = accept_input(book, "author")
        if result is True:
            break
        if result is False:
            break
        print(result)

    print(book)
    print(book2)
    print(book3)
