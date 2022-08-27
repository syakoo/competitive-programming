from collections import deque
from math import inf


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(m)]
    k = int(input())
    Cs = lmap(int, input().split())

    AB_dict = dict()
    for a, b in ABs:
        if a not in AB_dict:
            AB_dict[a] = [b]
        else:
            AB_dict[a].append(b)

        if b not in AB_dict:
            AB_dict[b] = [a]
        else:
            AB_dict[b].append(a)

    def find_dist(a, b, mapp):
        que = deque([a])
        ms = [0 for _ in range(n)]
        while not que.empty():
            _now = que.popleft()
            if _now == b:
                return ms[_now]

            for _nex in mapp[_now]:
                if ms[_nex] == 0:
                    ms[_nex] = ms[_now] + 1
                    que.append(_nex)

        return -1

    dists = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for ci in range(k-1):
        for cj in range(ci+1, k):
            d = find_dist(ci, cj, AB_dict)
            dists[ci][cj] = d
            dists[cj][ci] = d


if __name__ == '__main__':
    main()
