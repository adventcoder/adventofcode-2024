from collections.abc import Sequence

def table(input, dtype=None):
    rows = []
    for line in input.splitlines():
        row = line.split()
        if dtype is None:
            rows.append(row)
        else:
            rows.append(list(map(dtype, row)))
    return rows

def sliding_window(xs, size):
    if isinstance(xs, Sequence):
        for i in range(len(xs) - size + 1):
            yield xs[i : i + size]
    else:
        it = iter(xs)
        window = tuple(next(it) for _ in range(size))
        yield window
        for x in it:
            window = window[1:] + (x, )
            yield window
