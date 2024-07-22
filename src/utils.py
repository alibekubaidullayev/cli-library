from models import Book


def accept_input(book_instance: Book, field_name: str) -> bool:
    attribute_type = type(getattr(book_instance, field_name))

    while True:
        inp: str = input(f"Insert {field_name} ('X' to quit assignment)")
        if inp.lower() == "x":
            return False

        try:
            casted_inp = attribute_type(inp)
        except ValueError:
            print(
                f"Error casting input to {attribute_type.__name__}. Please, try again!"
            )
            continue

        try:
            setattr(book_instance, field_name, casted_inp)
            print(f"Successfully set {field_name} to {casted_inp}")
            return True
        except AttributeError as e:
            print(f"Error setting attribute: {e}. Please, try again!")
            continue
