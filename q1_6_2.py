import itertools
from sys import stdin

def solve_min(line_len, positions):
    min_t = None
    for pos in positions:
        t = min(line_len - pos, pos)
        min_t = t if min_t == None else max(min_t, t)
    return min_t

def solve_max(line_len, positions):
    max_t = None
    for pos in positions:
        t = max(line_len - pos, pos)
        max_t = t if max_t == None else max(max_t, t)
    return max_t


def main():
    lines = map(lambda str: map(lambda x: int(x), str.split(' ')), stdin.readlines())
    min_t = solve_min(lines[0][0], lines[1])
    max_t = solve_max(lines[0][0], lines[1])
    print('{} {}'.format(min_t, max_t))

main()
