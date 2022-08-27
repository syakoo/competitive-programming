
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    ans = 0
    if n == 1:
        print(As[0])
        return

    for l in range(n):
        x = 10**6
        for r in range(l, n):
            x = min(x, As[r])
            ans = max(ans, x * (r - l + 1))

    print(ans)


if __name__ == '__main__':
    main()
