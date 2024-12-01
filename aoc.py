import click
from functools import wraps
import time
import os
import requests
import browsercookie
import inspect
import re

year = 2024
input_path = 'inputs/day{day}.txt'

@click.group()
def main():
    pass

def puzzle(day=None, part=None):
    def decorator(func):
        nonlocal day, part
        if day is None:
            day = detect_day(func)
        if part is None:
            part = detect_part(func)

        @main.command()
        @click.pass_context
        @click.option('--debug', is_flag=True)
        @wraps(func)
        def decorated(ctx: click.Context, debug, *args, **kwargs):
            set_debug(ctx, debug)
            input = ctx.find_object(str)
            if input is None:
                input = get_input(day)
            print(f'Part {part}:', Answer(ctx.invoke, func, input, *args, **kwargs))

        return decorated
    return decorator

def detect_day(func):
    mod = inspect.getmodule(func)
    if m := re.fullmatch(r'day(\d+).py', os.path.basename(mod.__file__)):
        return int(m.group(1))
    raise ValueError('day could not be determined')

def detect_part(func):
    if m := re.fullmatch(r'part(\d+)', func.__name__):
        return int(m.group(1))
    raise ValueError('part could not be determined')

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
        file.write(input)

class Answer:
    def __init__(self, func, *args, **kwargs):
        start_time = time.perf_counter()
        self.value = func(*args, **kwargs)
        self.time = time.perf_counter() - start_time

    def __str__(self):
        answer_str = str(self.value) if self.value is not None else '<No answer>'
        return answer_str + f' [{format_time(self.time)}]'

def format_time(time):
    s = int(time)
    ms = (time - s) * 1000
    parts = []
    if s:
        parts.append('%d s' % s)
    parts.append('%.3f ms' % ms)
    return ' '.join(parts)

def set_debug(ctx, debug):
    ctx.meta['{__name__}.debug'] = debug

def debug():
    ctx = click.get_current_context()
    return ctx.meta.get('{__name__}.debug', False)

def dprint(*args, **kwargs):
    if debug():
        print(*args, **kwargs)
