
import math
import sys

sys.setrecursionlimit(10**6)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    t = int(input())

    for _ in range(t):
        s = input()
        if s > 'atcoder':
            print(0)
            continue

        ans = -1
        for i, si in enumerate(s):
            if si != 'a':
                if i > 0 and si > 't':
                    ans = i - 1
                else:
                    ans = i
                break

        print(ans)


if __name__ == '__main__':
    main()
