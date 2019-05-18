from sys import stdin


# Saruman's Army


def solve(n, r, x):
    ans = 0
    i = 0
    while i < len(x):
        # マークされていない，一番左の点
        left = x[i]
        i = i + 1

        # `left` の範囲内にある，一番遠い点を見つける
        while i < len(x) and x[i] <= left + r:
            i = i + 1

        # `x[i - 1]` をマークする
        p = x[i - 1]

        # `p` の範囲外にある，一番最初の点まで進める
        while i < len(x) and x[i] <= p + r:
            i = i + 1
        ans = ans + 1
    return ans


def main():
    lines = [[int(n) for n in l.split(' ')] for l in stdin.readlines()]
    n, r = lines[0]
    x = lines[1]
    ans = solve(n, r, x)
    print(ans)


if __name__ == '__main__':
    main()
