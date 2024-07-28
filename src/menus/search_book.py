from models import Menu, Screen

from controls import search_book


def book_search_menu_create(screen: Screen, name: str):
    book_search_menu = Menu(name)
    book_search_menu.add_element(
        lambda: search_book(
            screen,
            "title",
            input("Insert title for search: "),
        ),
        "Title",
    )
    book_search_menu.add_element(
        lambda: search_book(
            screen,
            "author",
            input("Insert author for search: "),
        ),
        "Author",
    )

    book_search_menu.add_element(
        lambda: search_book(
            screen,
            "year",
            input("Insert year for search: "),
        ),
        "Year",
    )

    book_search_menu.add_element(
        lambda: search_book(
            screen,
            "",
            input("Insert general prompt for search: "),
        ),
        "All",
    )

    return book_search_menu
