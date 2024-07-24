import json

DB_PATH = "db.json"


def read_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def write_dict_to_json(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def create(obj: object) -> None:
    db = read_json_file(DB_PATH)
    pass


def read(id: int) -> object:
    pass


def delete(id: int) -> None:
    pass
