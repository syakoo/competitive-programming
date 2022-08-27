from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    As = lmap(int, input().split())
    Bs = lmap(int, input().split())
    CDs = [lmap(int, input().split()) for _ in range(m)]

    adjs = [[] for _ in range(n)]
    for c, d in CDs:
        adjs[c-1].append(d-1)
        adjs[d-1].append(c-1)

    visited = [0]*n
    for vi in range(n):
        if visited[vi]:
            continue

        q = deque([vi])
        visited[vi] = 1
        asum = 0
        bsum = 0

        while q:
            vj = q.popleft()
            asum += As[vj]
            bsum += Bs[vj]

            for adj in adjs[vj]:
                if not visited[adj]:
                    q.append(adj)
                    visited[adj] = 1

        if asum != bsum:
            print('No')
            return

    print('Yes')


if __name__ == '__main__':
    main()
