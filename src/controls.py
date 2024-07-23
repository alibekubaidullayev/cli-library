from sys import dont_write_bytecode
import time
from typing import Union

from menu import Menu
from models import Book
from screen import Screen


def accept_input(screen: Screen, field_name: str) -> Union[bool, str]:
    if not hasattr(screen.context.get("book"), field_name):
        raise AttributeError(
            f"{screen.context.get('book')} has no attribute {field_name}"
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


def insert_attr(screen: Screen, attr: str) -> None:
    done_or_err: Union[bool, str] = accept_input(screen, attr)

    if isinstance(done_or_err, bool):
        if done_or_err:
            screen.set_context_info(str(screen.context.get("book")))
            print(f"{attr.capitalize()} inserted")
        else:
            print("Cancelling assignment")
    elif isinstance(done_or_err, str):
        print(done_or_err)
        time.sleep(0.5)

    time.sleep(0.7)
