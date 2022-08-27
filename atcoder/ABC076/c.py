# 8 min
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    t = input()
    ans = ""

    for si in range(len(s) - len(t), -1, -1):
        flg = True
        for ti in range(len(t)):
            if s[si + ti] != '?' and s[si + ti] != t[ti]:
                flg = False
                break

        if not flg:
            continue

        ans = s[:si] + t + s[si + ti + 1:]
        break

    print(ans.replace('?', 'a') if ans != "" else "UNRESTORABLE")


if __name__ == '__main__':
    main()
