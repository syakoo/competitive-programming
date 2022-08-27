# 2 min 57 sec

def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    Hs = [int(input()) for _ in range(n)]
    Hs.sort()
    ans = 10**9

    # O(n-k)
    for l in range(n - k + 1):
        r = l + k - 1
        ans = min(ans, Hs[r] - Hs[l])

    print(ans)


if __name__ == '__main__':
    main()
