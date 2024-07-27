import os
import json
from typing import Dict, Any, List

from custom_types import DatabaseError
from .consts import BOOK_TABLE_NAME, DB_PATH


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
