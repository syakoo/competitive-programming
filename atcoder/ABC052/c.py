# 10 min
from collections import defaultdict
from functools import reduce


def lmap(func, iter):
    return list(map(func, iter))


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


def main():
    n = int(input())
    MOD = 10**9 + 7
    f = create_factorizer_with_sieve(n)

    facts = defaultdict(int)
    for x in range(2, n+1):
        fs = f(x)
        for k, v in fs.items():
            facts[k] += v

    print(reduce(lambda p0, p1: p0*(p1 + 1) % MOD, facts.values(), 1))


if __name__ == '__main__':
    main()
