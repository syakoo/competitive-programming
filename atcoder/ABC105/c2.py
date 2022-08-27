import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    x = 0
    ans = []
    i = 0
    if n == 0:
        print(0)
        return

    while n != x:
        r = n % pow(2, i + 1)
        if r != x % pow(2, i + 1):
            x += pow(-2, i)
            ans.append('1')
        else:
            ans.append('0')
        i += 1

    print(''.join(ans[::-1]))


if __name__ == '__main__':
    main()
