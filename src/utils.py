import time
from typing import Union

from models import Book
from screen import Screen
from menu import Menu


def accept_input(screen: Screen, field_name: str) -> Union[bool, str]:
    if not hasattr(screen.context.get("book"), field_name):
        raise AttributeError(
            f"{screen.context.get("book")} has no attribute {field_name}"
        )

    attribute_type = type(getattr(screen.context.get("book"), field_name))

    inp: str = input(f"Insert {field_name} ('X' to quit assignment)")

    if inp.lower() == "x":
        return False

    try:
        casted_inp = attribute_type(inp)
    except ValueError:
        return f"Error casting input to {attribute_type.__name__}. Please, try again!"

    try:
        setattr(screen.context.get("book"), field_name, casted_inp)
    except AttributeError as e:
        return f"Error setting attribute: {e}. Please, try again!"

    return True


def book_inserter(attr: str) -> None:
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
