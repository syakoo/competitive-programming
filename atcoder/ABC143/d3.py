from bisect import bisect_left


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Ls = lmap(int, input().split())

    Ls.sort()
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            r = bisect_left(Ls, Ls[i]+Ls[j])
            ans += r - j - 1

    print(ans)


if __name__ == '__main__':
    main()
