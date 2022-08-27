def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Ls = lmap(int, input().split())

    cnts = [0]*10**4
    for l in Ls:
        cnts[l] += 1
    for i in range(1, 10**4):
        cnts[i] += cnts[i-1]

    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            Li, Lj = Ls[i], Ls[j]
            l = abs(Li-Lj)
            r = Li+Lj

            ans += cnts[r-1] - cnts[l]
            if l < Li < r:
                ans -= 1
            if l < Lj < r:
                ans -= 1

    print(ans//3)


if __name__ == '__main__':
    main()
