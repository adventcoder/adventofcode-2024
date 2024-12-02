
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
    for i in range(len(xs) - size + 1):
        yield xs[i : i + size]
