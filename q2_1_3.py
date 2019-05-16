from sys import stdin

# Lake Counting


def valid_pos(m, pos):
    x, y = pos
    vlen = len(m)
    hlen = len(m[0])
    return 0 <= y < vlen and 0 <= x < hlen


def dfs(m, pos):
    m[pos[1]][pos[0]] = '.'
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            x = pos[0] + dx
            y = pos[1] + dy
            if valid_pos(m, (x, y)) and m[y][x] == 'W':
                dfs(m, (x, y))


def solve(m):
    cnt = 0
    for y, row in enumerate(m):
        for x, col in enumerate(row):
            if col == 'W':
                dfs(m, (x, y))
                cnt = cnt + 1
    return cnt


def parse_line(l):
    return list(l.strip())


def main():
    m = [parse_line(l) for l in stdin.readlines()][1:]
    cnt = solve(m)
    print(cnt)


if __name__ == '__main__':
    main()
