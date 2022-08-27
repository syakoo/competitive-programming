# 14 min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    ans = 0

    if k == 0:
        print(n*n)
        return

    for b in range(k+1, n+1):
        x, y = n // b, n % b
        ans += (b - k)*x + max(0, y - k + 1)

    print(ans)


if __name__ == '__main__':
    main()
