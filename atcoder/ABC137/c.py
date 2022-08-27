# 5 min 9sec

import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ss = [input() for _ in range(n)]
    ss = lmap(lambda s: ''.join(sorted(s)), ss)
    cnts = dict()

    for s in ss:
        if s in cnts:
            cnts[s] += 1
        else:
            cnts[s] = 1

    ans = 0
    for s, v in cnts.items():
        ans += v * (v - 1) // 2

    print(ans)


if __name__ == '__main__':
    main()
