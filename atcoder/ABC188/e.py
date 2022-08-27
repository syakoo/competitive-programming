
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    As = lmap(int, input().split())
    XYs = [lmap(int, input().split()) for _ in range(m)]
    edge_froms = {}

    for x, y in XYs:
        if y in edge_froms:
            edge_froms[y].append(x)
        else:
            edge_froms[y] = [x]

    dp = [[math.inf, -math.inf] for _ in range(n + 1)]
    for ai, a in enumerate(As):
        ai += 1
        if ai not in edge_froms:
            dp[ai] = [a, -math.inf]
        else:
            for ai_from in edge_froms[ai]:
                dp[ai][0] = min(dp[ai_from][0], a, dp[ai][0])
                dp[ai][1] = max(dp[ai_from][1], a - dp[ai_from][0], dp[ai][1])

    print(max(dp, key=lambda x: x[1])[1])


if __name__ == '__main__':
    main()
