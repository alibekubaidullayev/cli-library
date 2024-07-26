from typing import Callable, Protocol, Union
from functools import wraps

from screen import Screen


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


def error_handler(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise Exception(f"Error occured in '{func.__name__}': {e}")

    return wrapper


class JSONSerializable(Protocol):
    def to_json(self) -> str: ...
