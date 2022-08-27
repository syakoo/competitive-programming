
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    MOD = 10**9 + 7
    cmb = [[0 for _ in range(n+1)] for _ in range(n+1)]
    cmb[1][1] = 1

    for i in range(n + 1):
        cmb[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            cmb[i][j] = (cmb[i - 1][j-1] + cmb[i - 1][j]) % MOD

    for i in range(1, k+1):
        print((cmb[n-k+1][i]*cmb[k-1][i-1]) % MOD)


if __name__ == '__main__':
    main()
