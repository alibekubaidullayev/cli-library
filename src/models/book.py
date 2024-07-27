import enum
from datetime import datetime
from typing import Optional, Dict

from core.consts import BOOK_TABLE_NAME, TITLE_MAX_SIZE, AUTHOR_MAX_SIZE
from db.base import get_max_id


class BookStatus(enum.Enum):
    IN_STOCK = "in_stock"
    ISSUED = "issued"


class Book:
    _id_counter: int = -1

    @classmethod
    def _generate_id(cls) -> int:
        cls._id_counter = get_max_id(BOOK_TABLE_NAME)
        cls._id_counter += 1
        return cls._id_counter

    def __init__(
        self,
        title: Optional[str] = None,
        author: Optional[str] = None,
        year: Optional[int] = None,
        status: BookStatus = BookStatus.IN_STOCK,
    ):
        self._title = ""
        self._author = ""
        self._year = 0
        self.fully_set = False

        if title:
            self.title = title
        if author:
            self.author = author
        if year:
            self.year = year

        self._status = status
        self._id = self._generate_id()

        if self._title and self._author and self._year:
            self.fully_set = True

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if not (1 <= len(value) <= TITLE_MAX_SIZE):
            raise AttributeError(f"Title must have size from 1 to {TITLE_MAX_SIZE}")
        self._title = value

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str) -> None:
        if not (1 <= len(value) <= AUTHOR_MAX_SIZE):
            raise AttributeError(f"Author must have size from 1 to {AUTHOR_MAX_SIZE}")
        self._author = value

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        if not (0 <= value <= datetime.now().year):
            raise AttributeError(
                f"The year must be between 0 and {datetime.now().year}"
            )
        self._year = value

    @property
    def status(self) -> BookStatus:
        return self._status

    @property
    def id(self) -> int:
        return self._id

    def change_status(self, status: BookStatus) -> None:
        self._status = status

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        parts = [f"id: {self.id}"]
        if self._title:
            parts.append(f"title: {self.title}")
        if self._author:
            parts.append(f"author: {self.author}")
        if self._year:
            parts.append(f"year: {self.year}")
        return f"{', '.join(parts)}"

    def to_dict(self) -> Dict:
        dict = {
            "id": self._id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status.value,
        }

        return dict
