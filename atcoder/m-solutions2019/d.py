from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ABs = [lmap(int, input().split()) for _ in range(n-1)]
    Cs = lmap(int, input().split())

    Cs.sort(reverse=True)

    adjs = [[] for _ in range(n)]
    for a, b in ABs:
        adjs[a-1].append(b-1)
        adjs[b-1].append(a-1)

    cls = [0]*n
    cls[0] = Cs[0]
    cur = 1
    q = deque([0])
    while q:
        vi = q.popleft()
        for vj in adjs[vi]:
            if cls[vj] == 0:
                cls[vj] = Cs[cur]
                cur += 1
                q.append(vj)

    print(sum(Cs) - Cs[0])
    print(*cls)


if __name__ == '__main__':
    main()
