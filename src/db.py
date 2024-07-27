import os
import json
from typing import Dict, Any, List

from utils import DictProtocol

DB_PATH = "db.json"


class DatabaseError(Exception):
    pass


class TableNotFoundError(DatabaseError):
    pass


class ItemNotFoundError(DatabaseError):
    pass


def read_db(file_path: str) -> Dict[str, Any]:
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise DatabaseError(f"DB file '{file_path}' not found.")
    except json.JSONDecodeError:
        raise DatabaseError(f"JSON reading error from file '{file_path}'")


def write_db(file_path: str, data: Dict[str, Any]) -> None:
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except IOError:
        raise DatabaseError(f"Error writing to the database file '{file_path}'.")


def init_db(tables: List[str]) -> None:
    if os.path.exists(DB_PATH):
        db_scheme = read_db(DB_PATH)
    else:
        db_scheme = {}

    for table in tables:
        if table not in db_scheme:
            db_scheme[table] = []

    write_db(DB_PATH, db_scheme)


def get_table(db: Dict[str, Any], table: str) -> list:
    db_table = db.get(table)
    if db_table is None:
        raise TableNotFoundError(f"No table called '{table}'")
    return db_table


def save_table(db: Dict[str, Any], table: str, db_table: list) -> None:
    db[table] = db_table
    write_db(DB_PATH, db)


def create(obj: DictProtocol, table: str) -> None:
    db = read_db(DB_PATH)
    db_table = get_table(db, table)
    db_table.append(obj.to_dict())
    save_table(db, table, db_table)


def read(id: int, table: str) -> Dict[str, Any]:
    db = read_db(DB_PATH)
    db_table = get_table(db, table)

    for item in db_table:
        if item.get("id") == id:
            return item

    raise ItemNotFoundError(f"Item with id '{id}' not found in table '{table}'.")


def list(table: str) -> List[Dict[str, Any]]:
    db = read_db(DB_PATH)
    db_table = get_table(db, table)
    return db_table


def delete(id: int, table: str) -> None:
    db = read_db(DB_PATH)
    db_table = get_table(db, table)

    for index, item in enumerate(db_table):
        if item.get("id") == id:
            del db_table[index]
            save_table(db, table, db_table)
            return

    raise ItemNotFoundError(f"Item with id '{id}' not found in table '{table}'.")


def create_book(obj: DictProtocol) -> None:
    create(obj, "books")


def read_book(id: int) -> Dict[str, Any]:
    return read(id, "books")


def delete_book(id: int) -> None:
    delete(id, "books")


def list_books() -> List[Dict[str, Any]]:
    return list("books")


def get_max_id(table: str) -> int:
    try:
        db = read_db(DB_PATH)
        db_table = get_table(db, table)
        max_id = max(item.get("id", -1) for item in db_table)
        return max_id
    except Exception:
        return -1
