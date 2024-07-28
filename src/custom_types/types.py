from typing import Protocol


class DictProtocol(Protocol):
    """
    Протокол для того, чтобы принимать классы у которых есть метод
    to_dict.
    """

    def to_dict(self) -> str: ...


class DatabaseError(Exception):
    pass


class TableNotFoundError(DatabaseError):
    pass


class ItemNotFoundError(DatabaseError):
    pass
