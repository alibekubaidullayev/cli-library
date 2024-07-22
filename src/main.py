import time
from menu import Menu
from screen import Screen


def exit_menu():
    exit()


def rand_action():
    print("$#)!$J!($)")
    time.sleep(1)


def some_action():
    print("SOME ACTION")
    time.sleep(1)


main_menu = Menu("Main Menu")

main_menu.add_element("Close", exit_menu)

first_menu = Menu("First")
second_menu = Menu("Second")
third_menu = Menu("Third")


first_menu.add_element("Some", some_action)
second_menu.add_element("Some", some_action)
third_menu.add_element("Rand", rand_action)

main_menu.available = [first_menu, second_menu, third_menu]

screen = Screen(main_menu)

# Loop to continuously render the menu and take input
while True:
    screen.render()
