from bisect import bisect_left
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    x = int(input())
    cnts = [0]
    Z = set('123456789')
    for c in s:
        if cnts[-1] > x:
            break
        if c in Z:
            cnts.append(cnts[-1]*(int(c) + 1))
        else:
            cnts.append(cnts[-1] + 1)

    def search(x: int) -> str:
        i = bisect_left(cnts, x)
        if cnts[i] == x and s[i-1] not in Z:
            return s[i-1]

        return search((x - 1) % cnts[i-1] + 1)

    print(search(x))


if __name__ == '__main__':
    main()
