import sys

sections = sys.stdin.read().strip().split("\n\n")
R = [[int(x) for x in line.split("-")] for line in sections[0].splitlines()]
Q = [int(line) for line in sections[1].splitlines()]


def part1():
    return sum(any(r[0] <= q <= r[1] for r in R) for q in Q)


def part2():
    events = sorted([(r[0], 0) for r in R] + [(r[1], 1) for r in R])

    total = 0
    depth = 0
    start = None
    for pos, event_type in events:
        if event_type == 0:
            # range start
            if depth == 0:
                start = pos
            depth += 1
        else:
            # range end
            if depth == 1:
                total += pos - start + 1
            depth -= 1
    return total


print(part1())
print(part2())
