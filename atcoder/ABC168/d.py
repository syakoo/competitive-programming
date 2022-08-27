from collections import deque


def main():
    n, m = map(int, input().split())
    es = [[] for _ in range(n+1)]
    ans = [0 for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        es[a].append(b)
        es[b].append(a)

    q = deque([1])
    while len(q) > 0:
        p = q.popleft()

        for t in es[p]:
            if ans[t] > 0:
                continue
            ans[t] = p
            q.append(t)

    if 0 in ans[2:]:
        print("No")
    else:
        print("Yes")
        for a in ans[2:]:
            print(a)


if __name__ == '__main__':
    main()
