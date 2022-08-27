from collections import defaultdict


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    Cs = lmap(int, input().split())
    cnts = defaultdict(int)
    for c in Cs[:k]:
        cnts[c] += 1
    cnt = len(cnts)

    ans = cnt
    for l in range(n - k):
        r = l + k
        if Cs[r] not in cnts or cnts[Cs[r]] == 0:
            cnt += 1
            cnts[Cs[r]] += 1
        else:
            cnts[Cs[r]] += 1
        if cnts[Cs[l]] == 1:
            cnt -= 1
            cnts[Cs[l]] -= 1
        else:
            cnts[Cs[l]] -= 1
        ans = max(ans, cnt)

    print(ans)


if __name__ == '__main__':
    main()
