from typing import Protocol


class DictProtocol(Protocol):
    def to_dict(self) -> str: ...


class DatabaseError(Exception):
    pass


class TableNotFoundError(DatabaseError):
    pass


class ItemNotFoundError(DatabaseError):
    pass
