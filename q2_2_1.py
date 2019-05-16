from sys import stdin


# 硬貨の問題
def solve(coins, price):
    ans = 0
    for c, amount in coins:
        n_use = min(price // c, amount)
        price = price - n_use * c
        ans = ans + n_use
    return ans


def main():
    *cnts, price = [int(n) for n in stdin.readlines()[0].split(' ')]
    coins = list(zip([1, 5, 10, 50, 100, 500], cnts))
    coins.reverse()
    ans = solve(coins, price)
    print(ans)


if __name__ == '__main__':
    main()
