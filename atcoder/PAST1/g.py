from itertools import product


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = [lmap(int, input().split()) for _ in range(n-1)]
    ans = -10**9

    for gs in product(*([[0, 1, 2]]*n)):
        metric = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if gs[i] == gs[j]:
                    metric += As[i][j - i - 1]

        ans = max(ans, metric)

    print(ans)


if __name__ == '__main__':
    main()
