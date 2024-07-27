from controls import add_book, clean_book, search_book
from core import BOOK_TABLE_NAME, init_db
from models import Menu, Screen
from utils import insert_attr

init_db([BOOK_TABLE_NAME])


def main():
    root_menu = Menu("Main Menu", root=True)
    screen = Screen(root_menu)

    book_add_menu = Menu("Add Book")
    book_add_menu.add_element(lambda: insert_attr(screen, "title", "book"), "Title")
    book_add_menu.add_element(lambda: insert_attr(screen, "author", "book"), "Author")
    book_add_menu.add_element(lambda: insert_attr(screen, "year", "book"), "Year")
    book_add_menu.add_element(lambda: clean_book(screen), "Clean")
    book_add_menu.add_element(lambda: add_book(screen), "Confirm")

    book_search_menu = Menu("Search")
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

    root_menu.add_element(book_add_menu)
    root_menu.add_element(book_search_menu)

    while True:
        screen.render()


if __name__ == "__main__":
    main()
