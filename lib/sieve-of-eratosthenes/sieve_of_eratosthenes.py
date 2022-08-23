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


print(sieve_of_eratosthenes(5))  # [2, 3, 5]
print(sieve_of_eratosthenes(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
