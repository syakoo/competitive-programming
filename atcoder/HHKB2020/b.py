
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    Sss = [input() for _ in range(h)]
    ans = 0

    for hi in range(h):
        for wi in range(w):
            if Sss[hi][wi] == '.':
                if hi < h - 1 and Sss[hi + 1][wi] == '.':
                    ans += 1
                if wi < w - 1 and Sss[hi][wi + 1] == '.':
                    ans += 1

    print(ans)


if __name__ == '__main__':
    main()
