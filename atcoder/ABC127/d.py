import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    As = lmap(int, input().split())
    BCs = [lmap(int, input().split()) for _ in range(m)]
    As.sort(reverse=True)
    As += [0]
    BCs.sort(reverse=True, key=lambda x: x[1])
    BCs += [(0, 0)]

    ans = 0
    ai = 0
    bci = 0
    cnt = 0
    while cnt < n:
        if As[ai] > BCs[bci][1]:
            ans += As[ai]
            ai += 1
            cnt += 1
        else:
            num = min(n - cnt, BCs[bci][0])
            ans += BCs[bci][1] * num
            cnt += num
            bci += 1

    print(ans)


if __name__ == '__main__':
    main()
