from time import sleep
from typing import Union, List, Any, Dict

from models.screen import Screen, Book


def accept_input(
    screen: Screen,
    field_name: str,
    cntx_obj_name: str,
) -> Union[bool, str]:
    """
    Записывает в поле (field_name) объекта из контекста (cntx_obj_name)
    при этом кастит вводимый в inp значение в тип (field_name).
    Возвращает либо False (отмена записи), True (успешная запись) либо
    текст ошибки. Данная функция работает в связке с insert_attr.
    Использован подход 'error as the value'.
    """
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
    """
    Работает непосредственно экраном для печати ошибок, либо сообщений об отмене, либо успехе.
    """
    done_or_err: Union[bool, str] = accept_input(screen, attr, context_object)

    if isinstance(done_or_err, bool):
        if done_or_err:
            screen.set_context_info(str(screen.context.get(context_object)))
            print(f"{attr.capitalize()} inserted")
        else:
            print("Cancelling assignment")
    elif isinstance(done_or_err, str):
        print(done_or_err)
        sleep(0.6)

    sleep(0.4)


def get_book_list(dicts: List[Dict[str, Any]]) -> List[Book]:
    result: List[Book] = []

    for dct in dicts:
        new_book = Book()
        new_book.from_dict(dct)
        result.append(new_book)

    return result
