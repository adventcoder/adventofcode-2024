from aoc import get_input, submit
from dataclasses import dataclass

#TODO: cleanup/part 2 is super slow

def compact1(packed):
    disk = []
    for i, c in enumerate(packed):
        id = i // 2 if i % 2 == 0 else None
        size = int(c)
        for _ in range(size):
            disk.append(id)

    start = 0
    end = len(disk) - 1
    while True:
        while disk[start] is not None:
            start += 1
        while disk[end] is None:
            end -= 1
        if start > end:
            break
        disk[start] = disk[end]
        disk[end] = None

    return sum(i * id for i, id in enumerate(disk) if id is not None)

@dataclass
class File:
    id: int
    start: int
    size: int

def compact2(packed):
    files = []
    start = 0
    for i, c in enumerate(packed):
        size = int(c)
        if i % 2 == 0:
            files.append(File(len(files), start, size))
        start += size

    disk = list(files)
    for file in reversed(files):
        for i in range(len(disk)):
            if disk[i] == file:
                break
            a, b = disk[i : i + 2]
            if b.start - a.start - a.size >= file.size:
                file.start = a.start + a.size
                disk.remove(file)
                disk.insert(i + 1, file)
                break

    checksum = 0
    for file in disk:
        for i in range(file.size):
            checksum += (file.start + i) * file.id
    return checksum

packed = get_input(9).strip()
submit(compact1(packed))
submit(compact2(packed))
