import sys

IN = sys.stdin.read()


def find_best(numbers: list[int], digits: int) -> int:
    if digits <= 0:
        return 0

    # find max in valid range (must leave enough digits after it)
    valid_range = len(numbers) - digits + 1
    v = max(numbers[:valid_range])
    vi = numbers.index(v)

    return v * (10 ** (digits - 1)) + find_best(numbers[vi + 1 :], digits - 1)


def solve(digits: int) -> int:
    return sum(find_best([int(c) for c in line.strip()], digits) for line in IN.splitlines())


print(solve(2))
print(solve(12))
