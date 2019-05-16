from sys import stdin
from collections import deque
from enum import Enum, auto

# 迷路の最短路を求める


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


def neighborpos(m, pos, direction):
    x, y = pos
    if direction == Direction.UP:
        return (x, y - 1)
    elif direction == Direction.DOWN:
        return (x, y + 1)
    elif direction == Direction.LEFT:
        return (x - 1, y)
    else:
        return (x + 1, y)


def validpos(m, pos):
    x, y = pos
    vlen = len(m)
    hlen = len(m[0])
    return 0 <= y < vlen and 0 <= x < hlen


# ゴールまでの距離を幅優先探索で求める
def solve(m, s, g):
    sx, sy = s
    gx, gy = g
    q = deque([s])
    d = [[None] * len(m[0]) for i in range(len(m))]
    d[sy][sx] = 0
    while len(q) > 0:
        x, y = q.popleft()
        if x == gx and y == gy:
            break
        for direction in Direction:
            npos = neighborpos(m, (x, y), direction)
            (nx, ny) = npos
            if validpos(m, npos) and m[ny][nx] != '#' and d[ny][nx] == None:
                q.append(npos)
                d[ny][nx] = d[y][x] + 1
    return d[gy][gx]

def findchar(m, c):
    for y, row in enumerate(m):
        for x, col in enumerate(row):
            if col == c:
                return x, y
    return None


def main():
    m = [list(l.strip()) for l in stdin.readlines()[1:]]
    s = findchar(m, 'S')
    g = findchar(m, 'G')
    mindist = solve(m, s, g)
    print(mindist)


if __name__ == '__main__':
    main()
