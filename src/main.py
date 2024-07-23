from menu import Menu
from screen import Screen


root_menu = Menu("Main Menu", root=True)
root_menu.add_control(name="Exit", action=lambda: exit(), key="x")
root_menu.add_control(name="Hello", action=lambda: print("Hello"))

root_menu.add_element(
    name="sad",
    action=lambda: print("SAD"),
)

root_menu.add_element(
    name="as",
    action=lambda: print("as"),
)

root_menu.add_element(
    name="asd",
    action=lambda: print("asd"),
)

on_menu = Menu("One")
root_menu.add_element(on_menu)

screen = Screen(root_menu)

while True:
    screen.render()
