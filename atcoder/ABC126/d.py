from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    UVWs = [lmap(int, input().split()) for _ in range(n-1)]

    adjs = [[] for _ in range(n)]
    for u, v, w in UVWs:
        adjs[u - 1].append((v - 1, w % 2))
        adjs[v - 1].append((u - 1, w % 2))

    colors = [-1]*n
    q = deque([0])
    colors[0] = 0
    while q:
        vi = q.popleft()
        for vj, wj in adjs[vi]:
            if colors[vj] == -1:
                colors[vj] = colors[vi] ^ wj
                q.append(vj)

    print('\n'.join(map(str, colors)))


if __name__ == '__main__':
    main()
