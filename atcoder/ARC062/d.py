# 12 min
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()

    ans = 0
    cnt = 0
    for si in s[::-1]:
        if si == 'g':
            cnt += 1
        else:
            if cnt > 0:
                ans += cnt // 2
                cnt %= 2
            cnt -= 1

    print(ans + cnt // 2)


if __name__ == '__main__':
    main()
