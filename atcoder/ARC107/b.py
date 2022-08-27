# NOT CLEARED

def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    ans = 0

    for m in range(2, 2*n+1):
        ans += f(n, m)*f(n, m-k)

    print(ans)


def f(n: int, m: int) -> int:
    if n < m-1:
        return 2*n - m + 1
    return m-1


if __name__ == '__main__':
    main()
