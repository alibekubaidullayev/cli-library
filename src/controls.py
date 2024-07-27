import time
from typing import Union

from models import Book
from screen import Screen
from db import create_book


def accept_input(
    screen: Screen,
    field_name: str,
    cntx_obj_name: str,
) -> Union[bool, str]:
    if not hasattr(screen.context.get(cntx_obj_name), field_name):
        raise AttributeError(
            f"{screen.context.get(cntx_obj_name)} has no attribute {field_name}"
        )

    attribute_type = type(getattr(screen.context.get(cntx_obj_name), field_name))

    inp: str = input(f"Insert {field_name} ('X' to quit assignment)")

    if inp.lower() == "x":
        return False

    try:
        casted_inp = attribute_type(inp)
    except ValueError:
        return f"Error casting input to {attribute_type.__name__}. Please, try again!"

    try:
        setattr(screen.context.get(cntx_obj_name), field_name, casted_inp)
    except AttributeError as e:
        return f"Error setting attribute: {e}. Please, try again!"

    return True


def insert_attr(screen: Screen, attr: str, context_object: str) -> None:
    done_or_err: Union[bool, str] = accept_input(screen, attr, context_object)

    if isinstance(done_or_err, bool):
        if done_or_err:
            screen.set_context_info(str(screen.context.get(context_object)))
            print(f"{attr.capitalize()} inserted")
        else:
            print("Cancelling assignment")
    elif isinstance(done_or_err, str):
        print(done_or_err)
        time.sleep(0.5)

    time.sleep(0.7)


def clean_book(screen: Screen) -> None:
    screen.context["book"] = Book()
    screen.clean_context_info()


def add_book(screen: Screen) -> None:
    book = screen.context["book"]
    create_book(book)
    clean_book(screen)
