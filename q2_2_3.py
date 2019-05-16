from sys import stdin


# 辞書順最小の問題
def solve(s):
    ans = ''
    while len(s) > 0:
        fst, last = s[0], s[-1]
        s_rev = s[::-1]
        if s < s_rev:
            ans = ans + fst
            s = s[1:]
        else:
            ans = ans + last
            s = s[:-1]
    return ans


def main():
    s = stdin.readlines()[1].strip()
    ans = solve(s)
    print(ans)


if __name__ == '__main__':
    main()
