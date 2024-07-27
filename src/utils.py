from typing import Protocol


class DictProtocol(Protocol):
    def to_dict(self) -> str: ...
