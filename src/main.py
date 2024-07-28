from controls.controls import all_books
from core import BOOK_TABLE_NAME, init_db
from menus import book_add_menu_create, book_search_menu_create
from models import Menu, Screen

init_db([BOOK_TABLE_NAME])


def main():
    root_menu = Menu("Main Menu", root=True)
    screen = Screen(root_menu)

    book_add_menu = book_add_menu_create(screen, "Add Book")
    book_search_menu = book_search_menu_create(screen, "Search")

    book_all_menu = Menu("All Books")
    book_all_menu.add_element(lambda: all_books(screen), "Print All Books")

    root_menu.add_element(book_add_menu)
    root_menu.add_element(book_search_menu)
    root_menu.add_element(book_all_menu)

    while True:
        screen.render()


if __name__ == "__main__":
    main()
