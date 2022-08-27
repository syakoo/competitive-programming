from collections import defaultdict


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

    factorization = create_factorizer_with_sieve(n)
    facts = defaultdict(int)
    for i in range(2, n+1):
        res = factorization(i)

        for k, v in res.items():
            facts[k] += v

    n2 = 0
    n4 = 0
    n14 = 0
    n24 = 0
    n74 = 0
    for v in facts.values():
        if v >= 74:
            n74 += 1
        if v >= 24:
            n24 += 1
        if v >= 14:
            n14 += 1
        if v >= 4:
            n4 += 1
        if v >= 2:
            n2 += 1

    ans = (n4*(n4-1)//2*(n2-2) + n14*(n4-1) + n24*(n2-1) + n74)
    print(ans)


if __name__ == '__main__':
    main()
