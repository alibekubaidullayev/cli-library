from controls import clean_book, insert_attr, add_book
from menu import Menu
from screen import Screen

from db import init_db

init_db(["books"])

root_menu = Menu("Main Menu", root=True)
screen = Screen(root_menu)

book_add_menu = Menu("Add Book")
book_add_menu.add_element(lambda: insert_attr(screen, "title", "book"), "Title")
book_add_menu.add_element(lambda: insert_attr(screen, "author", "book"), "Author")
book_add_menu.add_element(lambda: insert_attr(screen, "year", "book"), "Year")
book_add_menu.add_element(lambda: clean_book(screen), "Clean")
book_add_menu.add_element(lambda: add_book(screen), "Confirm")

root_menu.add_element(book_add_menu)
root_menu.add_element(Menu("dsa"))


while True:
    screen.render()
