import sys
import time
from typing import Callable, Union

from menu import Menu


class Screen:
    def __init__(self, menu: Menu) -> None:
        self.menu = menu

    def set_new_menu(self, new_menu: Menu) -> None:
        new_menu.previous = self.menu
        self.menu = new_menu

    def render(self) -> None:
        sys.stdout.write("\0337")
        self.menu.draw_menu()
        self.take_action(input("Choose an option: "))
        time.sleep(0.1)
        sys.stdout.write("\0338\033[J")
        sys.stdout.flush()

    def take_action(self, inp: str) -> None:
        action: Union[Menu, Callable] = self.menu.get_mapping()[inp.upper()]
        if isinstance(action, Menu):
            self.set_new_menu(action)
        elif callable(action):
            action()

    def go_previous(self) -> None:
        if self.menu.previous:
            self.set_new_menu(self.menu.previous)
