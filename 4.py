import sys

M = [list(line) for line in sys.stdin.read().splitlines()]
H, W = len(M), len(M[0])


def count_neighbors(x, y, m):
    return sum(
        0 <= x + dx < W and 0 <= y + dy < H and m[y + dy][x + dx] == "@" for dx in (-1, 0, 1) for dy in (-1, 0, 1)
    )


def should_remove(x, y, m):
    return m[y][x] == "@" and count_neighbors(x, y, m) < 5


def part1():
    return sum(should_remove(x, y, M) for y in range(H) for x in range(W))


def part2():
    total = 0
    while True:
        to_remove = [(x, y) for y in range(H) for x in range(W) if should_remove(x, y, M)]
        if not to_remove:
            break
        total += len(to_remove)
        for x, y in to_remove:
            M[y][x] = "."
    return total


print(part1())
print(part2())
