
import math


def lmap(func, iter):
    return list(map(func, iter))


def bin_search(xs: list, a: int) -> int:
    l, r = 0, len(xs) - 1

    while r - l > 1:
        m = (r + l) // 2
        if xs[m] >= a:
            r = m
        else:
            l = m

    if xs[l] >= a:
        return l
    else:
        return r


def main():
    s = input()
    t = input()
    sn = len(s)
    ans = 0

    s_dict = dict()
    for i, s in enumerate(s):
        if s in s_dict:
            s_dict[s].append(i)
        else:
            s_dict[s] = [i]

    for k in s_dict.keys():
        s_dict[k].append(s_dict[k][0] + sn)

    for ti in t:
        if ti not in s_dict:
            print(-1)
            return
        cur = ans % sn
        idx = bin_search(s_dict[ti], cur)

        ans += s_dict[ti][idx] - cur + 1

    print(ans)


if __name__ == '__main__':
    main()
