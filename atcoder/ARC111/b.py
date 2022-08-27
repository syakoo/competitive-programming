# 22min
from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ABs = [lmap(int, input().split()) for _ in range(n)]
    adjs = [[] for _ in range(400000)]
    ans = 0

    for a, b in ABs:
        adjs[a-1].append(b-1)
        adjs[b-1].append(a-1)

    checked = [False] * len(adjs)

    for i in range(len(adjs)):
        if checked[i] or len(adjs[i]) == 0:
            continue

        cnt = 0
        is_tree = True
        que = deque([(i, 0)])
        while len(que):
            n_i, _from = que.popleft()
            if checked[n_i]:
                is_tree = False
                continue
            cnt += 1
            checked[n_i] = True

            for n_j in adjs[n_i]:
                if _from == n_j:
                    continue
                que.append((n_j, n_i))

        if is_tree:
            ans += cnt - 1
        else:
            ans += cnt

    print(ans)


if __name__ == '__main__':
    main()
