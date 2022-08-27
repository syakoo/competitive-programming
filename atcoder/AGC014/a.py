
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b, c = map(int, input().split())
    max_loop = 10**8
    cnt = 0

    while cnt < max_loop and a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        a, b, c = b//2 + c//2, a//2 + c//2, a//2 + b//2
        cnt += 1

    print(cnt if cnt < max_loop else -1)


if __name__ == '__main__':
    main()
