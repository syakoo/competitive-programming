
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    As = lmap(int, input().split())
    Bs = lmap(int, input().split())
    anss = []

    for a in As:
        if a not in Bs:
            anss.append(a)

    for b in Bs:
        if b not in As:
            anss.append(b)

    anss.sort()
    print(*anss)
