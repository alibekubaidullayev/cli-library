import sys
import time
from typing import Callable, Union

from menu import Menu


class Screen:
    def __init__(self, menu: Menu) -> None:
        self.menu = menu
        self.context = {}

    def set_new_menu(self, new_menu: Menu) -> None:
        new_menu.set_prev(self.menu)
        self.menu = new_menu

    def render(self) -> None:
        sys.stdout.write("\0337")
        self.menu.draw_menu()
        self.take_action(input("Choose an option: "))
        time.sleep(0.1)
        sys.stdout.write("\0338\033[J")
        sys.stdout.flush()

    def take_action(self, inp: str) -> None:
        action: Union[Callable, Menu] = self.menu.get_mapping()[inp.lower()]
        if isinstance(action, Menu):
            self.set_new_menu(action)
        elif callable(action):
            action()
