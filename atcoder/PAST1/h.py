from itertools import product


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Cs = lmap(int, input().split())
    q = int(input())
    Ss = [lmap(int, input().split()) for _ in range(q)]

    C_subs = [0] * n
    odd_min = min(Cs[::2])
    all_min = min(Cs)
    odd_sub = 0
    all_sub = 0

    for s in Ss:
        if s[0] == 1:
            _, x, a = s
            if not x & 1:
                if Cs[x - 1] - C_subs[x - 1] - all_sub >= a:
                    C_subs[x-1] += a
                    all_min = min(all_min, Cs[x-1] - C_subs[x-1])
            else:
                if Cs[x-1] - C_subs[x - 1] - all_sub - odd_sub >= a:
                    C_subs[x-1] += a
                    all_min = min(all_min, Cs[x-1] - C_subs[x-1])
                    odd_min = min(odd_min, Cs[x-1] - C_subs[x-1])
        elif s[0] == 2:
            _, a = s
            if odd_min >= a:
                odd_sub += a
                odd_min -= a
                all_min = min(all_min, odd_min)
        else:
            _, a = s
            if all_min >= a:
                all_sub += a
                all_min -= a
                odd_min -= a

    ans = 0

    for i in range(n):
        ans += C_subs[i] + all_sub
        if not i & 1:
            ans += odd_sub

    print(ans)


if __name__ == '__main__':
    main()
