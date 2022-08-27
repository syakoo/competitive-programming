from collections import defaultdict


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())

    cnts = defaultdict(int)
    for a in As:
        cnts[a] += 1

    ans = 0
    for a in As:
        ans += n - cnts[a]

    print(ans//2)


if __name__ == '__main__':
    main()
