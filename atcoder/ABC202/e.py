import sys
import bisect

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Ps = lmap(int, input().split())
    q = int(input())
    UDs = [lmap(int, input().split()) for _ in range(q)]

    adjs = [[] for _ in range(n)]
    for i, pi in enumerate(Ps):
        adjs[pi - 1].append(i + 1)

    v_cnts = [[] for _ in range(n)]
    depth_vs = [[] for _ in range(n+1)]

    def dfs(vi: int, depth: int, cnt: int):
        v_cnts[vi].append(cnt)
        depth_vs[depth].append(cnt)

        for vj in adjs[vi]:
            cnt = dfs(vj, depth + 1, cnt + 1)

        cnt += 1
        v_cnts[vi].append(cnt)
        return cnt

    dfs(0, 0, 0)

    for u, d in UDs:
        u -= 1
        if len(depth_vs[d]) == 0:
            print(0)
            continue

        l = bisect.bisect_left(depth_vs[d], v_cnts[u][0])
        r = bisect.bisect_right(depth_vs[d], v_cnts[u][1])
        print(r-l)


if __name__ == '__main__':
    main()
