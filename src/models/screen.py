import sys
import time
from typing import Callable, Optional, Union

from .book import Book
from .menu import Menu


class Screen:
    def __init__(self, menu: Menu) -> None:
        self.menu = menu
        self.context = {
            "book": Book(),
            "context_info": {},
        }

    @property
    def info(self) -> Optional[str]:
        return self.context["context_info"].get(self.menu)

    def set_new_menu(self, new_menu: Menu) -> None:
        new_menu.set_prev(self.menu)
        self.menu = new_menu

        if new_menu not in self.context["context_info"]:
            self.context["context_info"][new_menu] = ""

    def render(self) -> None:
        sys.stdout.write("\0337")

        self.menu.draw_menu()

        if self.info:
            print("Info:", self.info)

        self.take_action(input("$>"))
        time.sleep(0.05)

        sys.stdout.write("\0338\033[J")
        sys.stdout.flush()

    def take_action(self, inp: str) -> None:
        action: Union[Callable, Menu, None] = self.menu.get_mapping().get(inp.upper())
        if not action:
            print("No such key")
            time.sleep(0.5)
            return
        if isinstance(action, Menu):
            self.set_new_menu(action)
        elif callable(action):
            action()

    def set_context_info(self, info: Union[str, None]) -> None:
        self.context["context_info"][self.menu] = info

    def clean_context_info(self) -> None:
        self.set_context_info(None)
