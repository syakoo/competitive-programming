# 32 min

import math
import bisect


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    Hs = lmap(int, input().split())
    Ws = lmap(int, input().split())
    Hs.sort()
    Ws.sort()

    lhs = [0 for _ in range(n)]
    rhs = [0 for _ in range(n)]

    # O(n)
    for i in range(1, n):
        j = n - i - 1
        lhs[i] += lhs[i-1] + (Hs[i] - Hs[i-1]) if i % 2 == 1 else lhs[i-1]
        rhs[j] += rhs[j+1] + (Hs[j + 1] - Hs[j]) if j % 2 == 1 else rhs[j+1]

    ans = math.inf
    # O(m*log n)
    for w in Ws:
        idx = bisect.bisect_left(Hs, w)
        if idx >= n:
            idx = n - 1
        if idx % 2 == 0:
            ans = min(ans, lhs[idx] + rhs[idx] + abs(w - Hs[idx]))
        else:
            ans = min(ans, lhs[idx-1] + rhs[idx-1] + abs(w - Hs[idx - 1]),
                      lhs[idx+1] + rhs[idx+1] + abs(w - Hs[idx + 1]))

    print(ans)


if __name__ == '__main__':
    main()
