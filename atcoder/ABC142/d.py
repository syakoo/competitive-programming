# 5 min

import math


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


def main():
    a, b = map(int, input().split())
    ab_gcd = math.gcd(a, b)

    if ab_gcd == 1:
        print(1)
        return

    print(1 + len(factorization(ab_gcd)))


if __name__ == '__main__':
    main()
