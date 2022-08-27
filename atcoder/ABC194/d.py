import sys
sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ans = 0

    for i in range(n-1):
        ans += n / (n - i - 1)

    print(ans)


if __name__ == '__main__':
    main()
