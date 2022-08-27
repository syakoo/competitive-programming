from itertools import product


def main():
    n, m, x = map(int, input().split())
    CAs = [list(map(int, input().split())) for _ in range(n)]

    ans = 1 << 60
    for indices in product(*[(-1, i) for i in range(n)]):
        sumCAs = [0]*(m+1)
        for i in indices:
            if i == -1:
                continue
            for j in range(m+1):
                sumCAs[j] += CAs[i][j]

        if all(x <= a for a in sumCAs[1:]):
            ans = min(ans, sumCAs[0])

    if ans >= 1 << 60:
        ans = -1
    print(ans)


main()
