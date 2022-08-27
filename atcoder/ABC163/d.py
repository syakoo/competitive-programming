
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    ans = 0
    def f(n): return n*(n+1)//2

    for ki in range(k, n+2):
        ans = (ans + f(n) - f(n-ki) - f(ki - 1) + 1) % (10**9 + 7)

    print(ans % (10**9 + 7))


if __name__ == '__main__':
    main()
