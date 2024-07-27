import enum
from datetime import datetime
from typing import Any, Dict, Optional

from core.consts import AUTHOR_MAX_SIZE, BOOK_TABLE_NAME, TITLE_MAX_SIZE
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

    def _set_id(self, value: int) -> None:
        self._id = value

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
        if not (-2000 <= value <= datetime.now().year):
            raise AttributeError(
                f"The year must be between -2000 and {datetime.now().year}"
            )
        self._year = value

    @property
    def status(self) -> BookStatus:
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        self._status = BookStatus(value)

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
        return {
            "id": self._id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status.value,
        }

    def from_dict(self, dict: Dict[str, Any]) -> None:
        required_fields = ["id", "title", "author", "year", "status"]

        for field in required_fields:
            value = dict.get(field)
            if value is None:
                raise AttributeError(f"No {field} in given dict")
            setattr(self, field if field != "id" else "_id", value)

        self.fully_set = bool(self._title and self._author and self._year)

    def has_substring(self, prompt: str, attr_name: str = "") -> bool:
        prompt = prompt.lower()
        if attr_name:
            if not hasattr(self, "_" + attr_name):
                raise AttributeError(f"Book has no attribute '{attr_name}'")
            attr_value = getattr(self, "_" + attr_name)
            return prompt in str(attr_value).lower()

        return (
            prompt in self._title.lower()
            or prompt in self._author.lower()
            or prompt in str(self._year).lower()
        )
