import itertools
def solve(a):
    combs = itertools.combinations(a, 3)
    max_perimeter = 0
    for comb in combs:
        max_edge = max(comb)
        perimeter = sum(comb)
        if perimeter > max_perimeter and perimeter - max_edge > max_edge:
            max_perimeter = perimeter
    return max_perimeter

a = [2, 3, 4, 5, 10]
print(solve(a))
