from typing import Any, Dict, List

from core import BOOK_TABLE_NAME
from .base import create, delete, list, read


def create_book(book) -> None:
    create(book, BOOK_TABLE_NAME)


def read_book(id: int) -> Dict[str, Any]:
    return read(id, BOOK_TABLE_NAME)


def delete_book(id: int) -> None:
    delete(id, BOOK_TABLE_NAME)


def list_books() -> List[Dict[str, Any]]:
    return list(BOOK_TABLE_NAME)
