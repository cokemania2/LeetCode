N = int(input())

def func(x):
    if x < 5:
        if x == 3:
            return 1
        return -1
    if x % 5 == 0:
        return x // 5
    return (func(x - 3) + 1) if func(x - 3) != -1 else -1

print(func(N))