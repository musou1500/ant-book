import json

def memoize(fn):
    memo = {}
    def wrapper(*args, **kwargs):
        key = json.dumps({ 'args': args, 'kwargs': kwargs })
        if key not in memo:
            memo[key] = fn(*args, **kwargs)
        return memo [key]
    return wrapper

@memoize
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    for i in range(10):
        print(fib(i))
