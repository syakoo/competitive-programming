def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    t = input()

    dp = [[0]*(len(s)+1) for _ in range(len(t) + 1)]
    for ti in range(1, len(t)+1):
        for si in range(1, len(s)+1):
            if t[ti-1] == s[si-1]:
                dp[ti][si] = max(dp[ti][si], dp[ti-1][si-1]+1)
            else:
                dp[ti][si] = max(dp[ti][si-1], dp[ti-1][si])

    ans = []
    ti = len(t)
    si = len(s)
    while ti > 0 and si > 0:
        if s[si-1] == t[ti-1]:
            ans.append(s[si-1])
            si -= 1
            ti -= 1
        elif dp[ti][si-1] > dp[ti-1][si]:
            si -= 1
        else:
            ti -= 1

    print(''.join(reversed(ans)))


if __name__ == '__main__':
    main()
