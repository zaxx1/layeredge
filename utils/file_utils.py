import json
from configs.constants import REGISTER_PATH, FARM_PATH, PROXIES_PATH, FILED_PATH, SUCCESS_PATH, REFS_PATH

def read_json(path: str, encoding: str | None = None) -> list | dict:
    return json.load(open(path, encoding=encoding))

def read_file(path: str):
    with open(path, encoding='utf-8') as file:
        return [line.strip() for line in file]

def read_farm() -> list[str]:
    return read_file(FARM_PATH)

def read_register() -> list[str]:
    return read_file(REGISTER_PATH)

def read_proxies() -> list[str]:
    return read_file(PROXIES_PATH)

def read_refs() -> list[str]:
    return read_file(REFS_PATH)

def write_failed_account(private_key: str):
    with open(FILED_PATH, 'a', encoding="utf-8") as f:
        f.write(f'{private_key}\n')

def write_success_account(private_key: str):
    with open(SUCCESS_PATH, 'a', encoding="utf-8") as f:
        f.write(f'{private_key}\n')