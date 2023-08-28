import json


def read_json(path:str) -> dict:
    with open(path, 'r') as json_f:
        return json.load(json_f)