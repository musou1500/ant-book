from sys import stdin


# 区間スケジューリング問題
def solve(jobs):
    ans = 0
    t = 0
    for (start, end) in jobs:
        if start > t:
            ans = ans + 1
            t = end
    return ans


def main():
    t1, t2 = [[int(n) for n in l.split(' ')] for l in stdin.readlines()[1:]]
    jobs = list(zip(t1, t2))
    # 終了時間の早い順にソート
    jobs.sort(key = lambda job: job[1])
    ans = solve(jobs)
    print(ans)


if __name__ == '__main__':
    main()
