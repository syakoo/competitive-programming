def main():
    s = input()
    t = input()
    dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

    for si, sc in enumerate(s):
        for ti, tc in enumerate(t):
            if sc == tc:
                dp[si + 1][ti + 1] = max(dp[si + 1][ti],
                                         dp[si][ti + 1], dp[si][ti] + 1)
            else:
                dp[si + 1][ti + 1] = max(dp[si + 1][ti],
                                         dp[si][ti + 1])

    ans = []
    si, ti = len(s) - 1, len(t) - 1
    while si >= 0 and ti >= 0 and dp[si + 1][ti + 1] > 0:
        if s[si] == t[ti]:
            ans.append(s[si])
            si -= 1
            ti -= 1
        elif dp[si + 1][ti] > dp[si][ti + 1]:
            ti -= 1
        else:
            si -= 1

    print(''.join(ans[::-1]))


if __name__ == '__main__':
    main()
