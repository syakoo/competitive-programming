from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(m)]
    MOD = 10**9 + 7

    adjs = [[] for _ in range(n)]
    for a, b in ABs:
        adjs[a-1].append(b-1)
        adjs[b-1].append(a-1)

    q = deque([0])
    cnts = [0]*n
    cnts[0] = 1
    dists = [0]*n
    while q:
        vi = q.popleft()

        for vj in adjs[vi]:
            if dists[vj] == 0:
                dists[vj] = dists[vi] + 1
                q.append(vj)
            if dists[vj] == dists[vi] + 1:
                cnts[vj] += cnts[vi]
                cnts[vj] %= MOD

    print(cnts[-1])


if __name__ == '__main__':
    main()
