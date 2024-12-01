import os
import requests
import browsercookie

year = 2024
input_path = 'inputs/day{day}.txt'

def get_input(day):
    input = get_local_input(day)
    if input is None:
        input = get_server_input(day)
        put_local_input(day, input)
    return input

def get_server_input(day):
    res = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies=browsercookie.firefox())
    res.raise_for_status()
    return res.text

def get_local_input(day):
    path = input_path.format(day=day)
    if os.path.exists(path):
        with open(path, 'r') as file:
            return file.read()
    return None

def put_local_input(day, input):
    path = input_path.format(day=day)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as file:
        return file.write(input)
