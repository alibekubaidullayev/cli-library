import time
from typing import Union

from models.book import Book
from models.screen import Screen
from db import create_book


def clean_book(screen: Screen) -> None:
    screen.context["book"] = Book()
    screen.clean_context_info()


def add_book(screen: Screen) -> None:
    book = screen.context["book"]
    create_book(book)
    clean_book(screen)
