from collections import Counter


def lmap(func, iter):
    return list(map(func, iter))


def main():
    l, r = map(int, input().split())
    MOD = 2019

    cnts = Counter(x % MOD for x in range(l, min(r+1, l+2*MOD)))
    ans = MOD
    for x in cnts.keys():
        for y in cnts.keys():
            if x == y and cnts[x] < 2:
                continue
            ans = min(ans, x*y % MOD)

    print(ans)


if __name__ == '__main__':
    main()
