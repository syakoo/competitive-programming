
def main():
    n = int(input())
    sieve = [2 for _ in range(n+1)]
    sieve[1] = 1

    ans = 1

    for k in range(2, n+1):
        for j in range(k*2, n+1, k):
            sieve[j] += 1

        ans += sieve[k] * k

    print(ans)


if __name__ == '__main__':
    main()
