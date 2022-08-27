from collections import defaultdict


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    MOD = 10**9 + 7

    dp = [defaultdict(int) for _ in range(n + 1)]
    dp[0]['TTT'] = 1

    bads = set(['AGC', 'GAC', 'ACG', 'AGGC', 'ATGC', 'AGTC'])
    for i in range(1, n+1):
        for j in 'ACGT':
            for k in dp[i-1].keys():
                if k[1:] + j in bads or k + j in bads:
                    continue

                dp[i][k[1:] + j] += dp[i-1][k]
                dp[i][k[1:] + j] %= MOD

    print(sum(dp[n].values()) % MOD)


if __name__ == '__main__':
    main()
