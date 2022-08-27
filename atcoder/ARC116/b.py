
import math

MOD = 998244353


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    As.sort()
    ans = As[0]*As[0] % MOD
    a_sum = 0

    for i in range(1, n):
        a_sum = ((a_sum << 1) + As[i - 1]) % MOD
        ans += As[i] * (a_sum + As[i]) % MOD
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
