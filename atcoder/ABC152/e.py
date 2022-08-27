from functools import reduce
from collections import defaultdict


def create_factorizer_with_sieve(n: int):
    """エラトステネスの篩を用いた素因数分解🐍. O(n loglog n)

    Args:
        n (int): 最大数

    Returns:
        int -> dict: 素因数分解をする関数
    """
    # sieve of eratosthenes
    # O(n loglog n)
    sieve = [0] * (n + 1)
    sieve[1] = 1
    for i in range(2, int(n**0.5) + 1):
        if sieve[i] != 0:
            continue
        for j in range(i, n + 1, i):
            sieve[j] = i

    def factorization(m: int) -> dict:
        # O(log n)
        dic = {}
        if m == 1:
            return {1: 1}

        while m > 1:
            if sieve[m] == 0:
                sieve[m] = m

            if sieve[m] in dic:
                dic[sieve[m]] += 1
            else:
                dic[sieve[m]] = 1
            m //= sieve[m]

        return dic

    return factorization


def lmap(func, iter):
    return list(map(func, iter))


def inv(x: int, mod: int) -> int:
    return pow(x, mod-2, mod)


def main():
    n = int(input())
    As = lmap(int, input().split())
    MOD = 10**9 + 7

    fact = create_factorizer_with_sieve(max(As))
    lcms = defaultdict(int)
    for a in As:
        facts = fact(a)
        for k, v in facts.items():
            lcms[k] = max(lcms[k], v)

    A_lcm = reduce(lambda p0, p1: p0 *
                   pow(p1[0], p1[1], MOD) % MOD, lcms.items(), 1)
    print(sum(map(lambda x: (A_lcm*inv(x, MOD)) % MOD, As)) % MOD)


if __name__ == '__main__':
    main()
