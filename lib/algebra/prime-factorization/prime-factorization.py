def factorization(n: int) -> list:
    """素因数分解🐍. O(√n)"""
    arr = []
    temp = n
    for i in range(2, int(n**0.5)+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


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


if __name__ == "__main__":
    print(factorization(0))  # [[0, 1]]
    print(factorization(1))  # [[1, 1]]
    print(factorization(24))  # [[2, 3], [3, 1]]

    factor = create_factorizer_with_sieve(10**6)
    print(factor(1))  # {1: 1}
    print(factor(24))  # {3: 1, 2: 3}
    print(factor(1000))  # {5: 3, 2: 3}
    print(factor(100003))  # {100003: 1}
