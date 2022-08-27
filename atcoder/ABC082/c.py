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
    for k, v in cnts.items():
        if k > v:
            ans += v
        else:
            ans += v - k

    print(ans)


if __name__ == '__main__':
    main()
