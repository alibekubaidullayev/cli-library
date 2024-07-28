from time import sleep
from typing import List

from db import create_book, list_books
from utils import get_book_list
from models import Book, Screen


def clean_book(screen: Screen) -> None:
    screen.context["book"] = Book()
    screen.clean_context_info()


def add_book(screen: Screen) -> None:
    book: Book = screen.context["book"]
    create_book(book)
    clean_book(screen)


def search_book(screen: Screen, attr: str = "", prompt: str = "") -> List[Book]:
    books = get_book_list(list_books())
    if not prompt:
        return books

    result: List[Book] = []
    for book in books:
        if book.has_substring(prompt=prompt, attr_name=attr):
            result.append(book)

    screen.set_context_info("\n".join(map(str, result)))
    return result


def all_books(screen: Screen) -> None:
    books = get_book_list(list_books())
    for book in books:
        print(book)
        sleep(0.05)

    input("Press any key to leave...")
    screen.take_action("q")
