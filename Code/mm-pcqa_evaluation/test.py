import random


def is_monotonic(lst):
    increasing = all(x <= y for x, y in zip(lst, lst[1:]))
    decreasing = all(x >= y for x, y in zip(lst, lst[1:]))
    return increasing or decreasing


lst = [
    [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
    for i in range(10000000)
]


def is_true(x):
    return x == True


lst = list(map(is_monotonic, lst))

print(len(list(filter(is_true, lst))) / len(lst))
