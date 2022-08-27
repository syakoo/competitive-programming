from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def transpose(xss: list) -> list:
    result = [[0] * len(xss) for _ in xss]

    for i in range(len(xss)):
        for j in range(len(xss)):
            result[i][j] = xss[j][i]

    return result


def is_connected(xs: list, ys: list, k: int) -> bool:
    for x, y in zip(xs, ys):
        if x + y > k:
            return False

    return True


def cv_cnts(Ass, n, k) -> list:
    used = [0] * n
    connected_vects = []
    for i in range(n):
        if used[i]:
            continue

        used[i] = 1
        q = deque([i])
        cv = 1
        while q:
            i1 = q.popleft()
            for i2 in range(n):
                if used[i2]:
                    continue

                if is_connected(Ass[i1], Ass[i2], k):
                    used[i2] = 1
                    cv += 1
                    q.append(i2)

        connected_vects.append(cv)

    return connected_vects


def main():
    n, k = map(int, input().split())
    Ass = [lmap(int, input().split()) for _ in range(n)]
    MOD = 998244353

    cvs = cv_cnts(Ass, n, k) + cv_cnts(transpose(Ass), n, k)
    ans = 1
    for cv in cvs:
        for x in range(1, cv + 1):
            ans = (ans * x) % MOD
    print(ans)


if __name__ == '__main__':
    main()
