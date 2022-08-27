
def main():
    n, w = map(int, input().split())
    Ws = [(0, 0)] + [list(map(int, input().split())) for _ in range(n)]
    dp = [[0 for _ in range(n + 1)] for _ in range(w + 1)]

    for wi in range(1, w + 1):
        for ni in range(1, n + 1):
            if wi < Ws[ni][0]:
                dp[wi][ni] = dp[wi][ni - 1]
            else:
                dp[wi][ni] = max(
                    dp[wi][ni - 1], dp[wi - Ws[ni][0]][ni - 1] + Ws[ni][1])

    print(dp[w][n])


if __name__ == '__main__':
    main()
