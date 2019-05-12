def resolve(n, nums, s, acc = []):
    if n == 0:
        return acc if s == 0 else []
    elif s < 0:
        return [];
    else:
        for num in nums:
            comb = resolve(n - 1, nums, s - num, acc[:] + [num]);
            if len(comb) > 0:
                return comb
        return []

# kからn個の数字を選び，その和がmになる組み合わせを探す
# 同じ数字を複数回使っても良い
n = 4;
m = 10;
k = [1, 3, 5];
print(resolve(n, k, m));
