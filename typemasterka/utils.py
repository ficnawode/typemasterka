import json


def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}, returning empty dictionary")
        return {}


def dump_json(file_path, data_dict):
    with open(file_path, 'w') as file:
        json.dump(data_dict, file, indent=4)
