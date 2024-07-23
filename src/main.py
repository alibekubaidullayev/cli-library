from controls import insert_attr
from menu import Menu
from screen import Screen


root_menu = Menu("Main Menu", root=True)
screen = Screen(root_menu)

book_add_menu = Menu("Add Book")
book_add_menu.add_element(lambda: insert_attr(screen, "title"), "Title")
book_add_menu.add_element(lambda: insert_attr(screen, "author"), "Author")
book_add_menu.add_element(lambda: insert_attr(screen, "year"), "Year")
root_menu.add_element(book_add_menu)

root_menu.add_element(Menu("dsa"))


while True:
    screen.render()
