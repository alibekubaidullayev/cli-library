from typing import Any, Dict, List

from custom_types import TableNotFoundError, DictProtocol, ItemNotFoundError
from core import DB_PATH, read_db, write_db

def get_table(db: Dict[str, Any], table_name: str) -> list:
    db_table = db.get(table_name)
    if db_table is None:
        raise TableNotFoundError(f"No table called '{table_name}'")
    return db_table


def save_table(db: Dict[str, Any], table_name: str, db_table: list) -> None:
    db[table_name] = db_table
    write_db(DB_PATH, db)


def create(obj: DictProtocol, table_name: str) -> None:
    db = read_db(DB_PATH)
    db_table = get_table(db, table_name)
    db_table.append(obj.to_dict())
    save_table(db, table_name, db_table)


def read(id: int, table_name: str) -> Dict[str, Any]:
    db = read_db(DB_PATH)
    db_table = get_table(db, table_name)

    for item in db_table:
        if item.get("id") == id:
            return item

    raise ItemNotFoundError(f"Item with id '{id}' not found in table '{table_name}'.")


def list(table_name: str) -> List[Dict[str, Any]]:
    db = read_db(DB_PATH)
    db_table = get_table(db, table_name)
    return db_table


def delete(id: int, table_name: str) -> None:
    db = read_db(DB_PATH)
    db_table = get_table(db, table_name)

    for index, item in enumerate(db_table):
        if item.get("id") == id:
            del db_table[index]
            save_table(db, table_name, db_table)
            return

    raise ItemNotFoundError(f"Item with id '{id}' not found in table '{table_name}'.")


def get_max_id(table: str) -> int:
    try:
        db = read_db(DB_PATH)
        db_table = get_table(db, table)
        max_id = max(item.get("id", -1) for item in db_table)
        return max_id
    except Exception:
        return -1
