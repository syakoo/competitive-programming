
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    Ass = [lmap(int, input().split()) for _ in range(n)]

    def check(x: int):
        Bss = [[0] * (n+1)] + [[0] + lmap(lambda a: a <= x, As) for As in Ass]

        for h in range(1, n+1):
            for w in range(1, n+1):
                Bss[h][w] += Bss[h-1][w] + Bss[h][w-1] - Bss[h-1][w-1]

        for hl in range(n-k+1):
            for wl in range(n-k+1):
                if Bss[hl+k][wl+k] - Bss[hl+k][wl] - Bss[hl][wl+k] + Bss[hl][wl] >= (k**2 + 1) // 2:
                    return False

        return True

    l, r = -1, 10**9
    while r - l > 1:
        m = (l + r) // 2
        if check(m):
            l = m
        else:
            r = m

    print(r)


if __name__ == '__main__':
    main()
