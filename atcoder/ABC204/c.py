from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(m)]

    adjs = [[] for _ in range(n)]
    for a, b in ABs:
        adjs[a-1].append(b-1)

    ans = 0
    for s in range(n):
        used = [0]*n
        used[s] = 1
        q = deque([s])
        ans += 1

        while q:
            vi = q.popleft()
            for vj in adjs[vi]:
                if not used[vj]:
                    ans += 1
                    used[vj] = 1
                    q.append(vj)

    print(ans)


if __name__ == '__main__':
    main()
