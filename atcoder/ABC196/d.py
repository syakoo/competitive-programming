from itertools import combinations
import math


def lmap(func, iter):
    return list(map(func, iter))


def count(mp_dict: dict, h, w, d) -> int:
    if all(mp_dict.values()):
        return 1

    cnt = 0
    for k in range(d, h*w):
        if k not in mp_dict or mp_dict[k]:
            continue

        if k % w != w - 1 and k + 1 in mp_dict and not mp_dict[k+1]:
            n_mp = mp_dict.copy()
            n_mp[k] = True
            n_mp[k + 1] = True
            cnt += count(n_mp, h, w, k + 1)

        if k <= w * (h - 1) and k + w in mp_dict and not mp_dict[k+w]:
            n_mp = mp_dict.copy()
            n_mp[k] = True
            n_mp[k + w] = True
            cnt += count(n_mp, h, w, k + 1)

    return cnt


def main():
    h, w, a, b = map(int, input().split())
    ans = 0

    for mps in combinations(range(h*w), 2*a):
        mp_dict = {k: False for k in mps}
        ans += count(mp_dict, h, w, 0)

    print(ans)


if __name__ == '__main__':
    main()
