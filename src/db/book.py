from typing import Dict, List, Any

from core import BOOK_TABLE_NAME
from custom_types import DictProtocol
from .base import create, read, delete, list


def create_book(obj: DictProtocol) -> None:
    create(obj, BOOK_TABLE_NAME)


def read_book(id: int) -> Dict[str, Any]:
    return read(id, BOOK_TABLE_NAME)


def delete_book(id: int) -> None:
    delete(id, BOOK_TABLE_NAME)


def list_books() -> List[Dict[str, Any]]:
    return list(BOOK_TABLE_NAME)
