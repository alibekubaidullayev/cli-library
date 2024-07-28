import sys
import time
from typing import Callable, Optional, Union

from .book import Book
from .menu import Menu


class Screen:
    """
    Класс созданый для переключения между меню и правильного отображения контекста соотвествующей
    менюшки.

    Атрибуты:
    -   menu (Menu): отображаемая менюшка
    -   context (Dict): для хранения контекстной информации
    -   context["book"] (Book): временное хранилище для ново создаваемой книги
    -   context["context_info"] (str): для переключения между контекстной информацией разных меню
    -   info (str): результат выполения функции, или доп инфы для каждой менюшки

    """

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
        """
        Меняет нынешнее меню
        """
        new_menu.set_prev(self.menu)
        self.menu = new_menu

        if new_menu not in self.context["context_info"]:
            self.context["context_info"][new_menu] = ""

    def render(self) -> None:
        """
        Отрисовка нынешней меню
        """
        sys.stdout.write("\0337")

        self.menu.draw_menu()

        if self.info:
            print(self.info)
            self.menu.draw_frame()

        self.take_action(input("$>"))
        time.sleep(0.05)

        sys.stdout.write("\0338\033[J")
        sys.stdout.flush()

    def take_action(self, inp: str) -> None:
        """
        Либо вызывает фунцкию, которая хранится по определенному ключу (смотреть аннотацию класса Menu)
        либо меняет нынешнее меню
        """
        action: Union[Callable, Menu, None] = self.menu.get_mapping().get(inp.upper())
        if not action:
            print("No such key")
            time.sleep(0.5)
            return
        if isinstance(action, Menu):
            self.set_new_menu(action)
        elif callable(action):
            try:
                action()
            except Exception as e:
                print(e)
                time.sleep(1)

    def set_context_info(self, info: Union[str, None]) -> None:
        self.context["context_info"][self.menu] = info

    def clean_context_info(self) -> None:
        self.set_context_info(None)
