def sieve_of_eratosthenes(n):
    """O(n loglog n)"""
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


def lmap(func, iter):
    return list(map(func, iter))


def main():
    l, r = map(int, input().split())

    primes = sieve_of_eratosthenes(r)
    cnt = 0
    for p in primes:
        num = r//p - (l-1)//p
        cnt += num*num - num

    for x in range(max(2, l), r):
        cnt -= (r // x - 1)*2

    print(cnt)


if __name__ == '__main__':
    main()
