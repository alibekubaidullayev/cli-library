from menu import Menu
from screen import Screen
from utils import BookCreationContext, add_book_setup


root_menu = Menu("Main Menu", root=True)
screen: Screen = Screen(root_menu)

book_creation_context = BookCreationContext()
book_creation_menu = add_book_setup(book_creation_context)
root_menu.add_element(
    "Add book",
    # lambda: add_book_setup(screen, book_creation_context),
    book_creation_menu,
)

print(root_menu.elements)

while True:
    screen.render()

