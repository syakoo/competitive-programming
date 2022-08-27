
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, a, b = map(int, input().split())
    Xs = lmap(int, input().split())
    ans = 0
    for i in range(n-1):
        d = Xs[i+1] - Xs[i]
        ans += min(b, a * d)

    print(ans)


if __name__ == '__main__':
    main()
