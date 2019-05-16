from sys import stdin

# 部分和問題
def solve(s, nums, idx = 0):
    if idx == len(nums):
        return s == 0
    else:
        return solve(s - nums[idx], nums, idx + 1) or solve(s, nums, idx + 1)

def main():
    lines = stdin.readlines()
    s = int(lines[0])
    nums = list(map(lambda n: int(n), lines[1].split(' ')))
    print('Yes' if solve(s, nums) else 'No')

if __name__ == '__main__':
    main()
