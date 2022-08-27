
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    As = lmap(int, input().split())
    ans = 0
    r = 0
    s_a = 0
    for l in range(n):
        if l > 0:
            s_a -= As[l - 1]

        while s_a < k and r < n:
            s_a += As[r]
            r += 1

        if s_a < k:
            break
        ans += (n - r + 1)

    print(ans)


if __name__ == '__main__':
    main()
