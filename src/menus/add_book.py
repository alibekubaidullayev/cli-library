from models import Screen, Menu

from utils import insert_attr
from controls import clean_book, add_book


def book_add_menu_create(screen: Screen, name: str):
    book_add_menu = Menu(name)
    book_add_menu.add_element(lambda: insert_attr(screen, "title", "book"), "Title")
    book_add_menu.add_element(lambda: insert_attr(screen, "author", "book"), "Author")
    book_add_menu.add_element(lambda: insert_attr(screen, "year", "book"), "Year")
    book_add_menu.add_element(lambda: clean_book(screen), "Clean")
    book_add_menu.add_element(lambda: add_book(screen), "Confirm")

    return book_add_menu
