import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    s = input()
    t = input()

    ss = []
    for i, si in enumerate(s):
        if si == '0':
            ss.append(i)
    ts = []
    for i, ti in enumerate(t):
        if ti == '0':
            ts.append(i)

    if len(ss) != len(ts):
        print(-1)
        return

    ans = 0
    for s, t in zip(ss, ts):
        ans += 1 if t != s else 0

    print(ans)


if __name__ == '__main__':
    main()
