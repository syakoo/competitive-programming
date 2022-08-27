
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, a, b = map(int, input().split())
    s = input()
    cnt = 0
    bcnt = 1

    for si in s:
        if si == 'a' and a + b > cnt:
            cnt += 1
            print('Yes')
        elif si == 'b' and a + b > cnt and b >= bcnt:
            cnt += 1
            bcnt += 1
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()
