
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b, c = map(int, input().split())
    mx = max(a, b, c)
    sub_mxs = lmap(lambda x: mx - x, [a, b, c])
    odd_cnt = lmap(lambda x: x % 2, sub_mxs).count(1)

    ans = sum(map(lambda x: x//2, sub_mxs))
    if odd_cnt == 2:
        ans += 1
    elif odd_cnt == 1:
        ans += 2

    print(ans)


if __name__ == '__main__':
    main()
