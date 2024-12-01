import os
import requests
import browsercookie
import time

year = 2024
inputs_path = 'inputs'
input_path = os.path.join(inputs_path, 'day{day}.txt')

def get_input(day):
    input = get_local_input(day)
    if input is None:
        input = get_server_input(day)
        put_local_input(day, input)
    global start_time, part
    start_time = time.perf_counter()
    part = 1
    return input

def get_server_input(day):
    res = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies=browsercookie.firefox())
    res.raise_for_status()
    return res.text

def get_local_input(day):
    try:
        with open(input_path.format(day=day), 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None

def put_local_input(day, input):
    os.makedirs(inputs_path, exist_ok=True)
    with open(input_path.format(day=day), 'w') as file:
        return file.write(input)

def submit(answer):
    global start_time, part
    solve_time = time.perf_counter() - start_time
    print(f'{part}.', answer, f'[{format_time(solve_time)}]')
    part += 1
    start_time = time.perf_counter()

def format_time(time):
    s = int(time)
    ms = (time - s) * 1000
    parts = []
    if s:
        parts.append('%d s' % s)
    parts.append('%.3f ms' % ms)
    return ' '.join(parts)
