# 17 min
import bisect


def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b, q = map(int, input().split())
    INF = 10**12
    Ss = [int(input()) for _ in range(a)]
    Ts = [int(input()) for _ in range(b)]
    Xs = [int(input()) for _ in range(q)]
    Ss = [-INF] + Ss + [INF]
    Ts = [-INF*2] + Ts + [INF*2]

    for x in Xs:
        si = bisect.bisect_left(Ss, x)
        ti = bisect.bisect_left(Ts, x)

        ans = min(
            abs(x - Ss[si]) + abs(Ss[si] - Ts[ti]),
            abs(x - Ss[si]) + abs(Ss[si] - Ts[ti-1]),
            abs(x - Ss[si-1]) + abs(Ss[si-1] - Ts[ti]),
            abs(x - Ss[si-1]) + abs(Ss[si-1] - Ts[ti-1]),
            abs(x - Ts[ti]) + abs(Ts[ti] - Ss[si]),
            abs(x - Ts[ti]) + abs(Ts[ti] - Ss[si-1]),
            abs(x - Ts[ti-1]) + abs(Ts[ti-1] - Ss[si]),
            abs(x - Ts[ti-1]) + abs(Ts[ti-1] - Ss[si-1])
        )
        print(ans)


if __name__ == '__main__':
    main()
