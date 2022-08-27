
def factorization(n: int, sieve: list) -> set:
    s = set()
    temp = n
    while temp > 1:
        if sieve[temp] == 0:
            s.add(temp)
            temp  = 1
        else:
            s.add(sieve[temp])
            temp //= sieve[temp]

    return s


def sieve_of_eratosthenes(n):
    res = [0] * (n + 1)
    res[1] = 1
    for i in range(2, int(n**0.5) + 1):
        if res[i] != 0:
            continue
        for j in range(i, n + 1, i):
            if res[j] == 0:
                res[j] = i

    return res


def main():
    n = int(input())
    As = list(map(int, input().split()))
    sieve = sieve_of_eratosthenes(10**6)
    union_prs = set()
    intersect_prs = factorization(As[0], sieve)
    is_pairwise = True

    for a in As:
        prs = factorization(a, sieve)
        if is_pairwise & (not union_prs.isdisjoint(prs)):
            is_pairwise = False

        union_prs |= prs
        intersect_prs &= prs

    if intersect_prs:
        print('not coprime')
    elif is_pairwise:
        print('pairwise coprime')
    else:
        print('setwise coprime')


if __name__ == '__main__':
    main()
