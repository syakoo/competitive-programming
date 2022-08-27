# 25 min

def lmap(func, iter):
    return list(map(func, iter))


def f(Xs: list, Ys: list) -> list:
    n = len(Xs)
    cur = [0] * 2
    result = [n] * n

    while cur[0] < n:
        while cur[1] < n and Ys[cur[1]] <= Xs[cur[0]]:
            cur[1] += 1
        if cur[1] == n:
            break
        result[cur[0]] = cur[1]
        cur[0] += 1

    return result


def main():
    n = int(input())
    As = lmap(int, input().split())
    Bs = lmap(int, input().split())
    Cs = lmap(int, input().split())
    As.sort()
    Bs.sort()
    Cs.sort()

    ABs = f(As, Bs)
    BCs = f(Bs, Cs)
    BCs_sum = [0] * (n+1)

    for i in range(n-1, -1, -1):
        BCs_sum[i] = n - BCs[i] + BCs_sum[i+1]

    ans = 0
    for ab in ABs:
        ans += BCs_sum[ab]

    print(ans)


if __name__ == '__main__':
    main()
