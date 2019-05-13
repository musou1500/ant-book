import itertools
from sys import stdin

def bin_search(l, n):
    left = 0
    right = len(l)
    mid = right // 2
    while 0 < mid < len(l):
        if l[mid] == n:
            return True
        elif n < l[mid]:
            right = mid
        else:
            left = mid - 1
        mid = left + right // 2
    return False

# numsから4個の数字を選び，その和がsになる組み合わせを探す
# 同じ数字を複数回使っても良い
def solve(nums, s):
    # numsから2つ選んだ合計を記憶しておく
    nums2 = list(map(lambda nums: sum(nums), itertools.combinations(nums, 2)))
    nums2.sort()
    for num in nums2:
        # binary search
        if bin_search(nums2, s - num):
            return True
    return False


def main():
    lines = stdin.readlines()
    nums = map(lambda x: int(x), lines[1].split(' '))
    ans = 'Yes' if solve(nums, int(lines[0])) else 'No'
    print(ans)

if __name__ == '__main__':
    main()
