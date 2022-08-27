import math
<<<<<<< HEAD
=======
import sys

sys.setrecursionlimit(10**9)
>>>>>>> 6ff60da37a54d105f7c01a9afebacd742500d696


def lmap(func, iter):
    return list(map(func, iter))


def main():
<<<<<<< HEAD
    a, b, c, d = map(int, input().split())

    ccnt = b // c - math.ceil(a / c) + 1
    dcnt = b // d - math.ceil(a / d) + 1
    cd = c*d//math.gcd(c, d)
    cdcnt = b // cd - math.ceil(a / cd) + 1

    ans = max(0, 1+b-a-(ccnt + dcnt - cdcnt))
    print(ans)
=======
    pass
>>>>>>> 6ff60da37a54d105f7c01a9afebacd742500d696


if __name__ == '__main__':
    main()
