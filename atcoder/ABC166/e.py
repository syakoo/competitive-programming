
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    ms = [[0, 0] for _ in range(n)]

    for i, a in enumerate(As):
        l = i - a
        r = i + a
        if l >= 0:
            ms[l][0] += 1
        if r < n:
            ms[r][1] += 1

    ans = 0
    for l, r in ms:
        ans += l * r

    print(ans)


if __name__ == '__main__':
    main()
