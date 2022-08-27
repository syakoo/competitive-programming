import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    rot = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

    ans = []
    for si in s[::-1]:
        ans.append(rot[si])

    print(''.join(ans))


if __name__ == '__main__':
    main()
