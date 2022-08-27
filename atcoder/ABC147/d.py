# cheated

import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    MOD = 10**9 + 7

    if max(As) == 0:
        print(0)
        return
    mx_deg = math.ceil(math.log2(max(As)))
    ans = 0

    for deg in range(mx_deg + 1):
        zeron, onen = 0, 0
        bit = 1 << deg

        for a in As:
            if a & bit:
                onen += 1
            else:
                zeron += 1

        ans += zeron * onen * bit % MOD
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
