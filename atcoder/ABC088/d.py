# 9 min
from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    Sss = ['#'*(w+2) for _ in range(h+2)]

    b_cnt = 0
    for hi in range(h):
        row = input()
        Sss[hi+1] = '#' + row + '#'
        b_cnt += row.count('#')

    dist = [[-1]*(w+2) for _ in range(h+2)]
    dist[1][1] = 0
    q = deque([(1, 1)])
    while q:
        hi, wi = q.popleft()

        for dh, dw in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nh, nw = hi + dh, wi + dw
            if Sss[nh][nw] == '.' and dist[nh][nw] == -1:
                dist[nh][nw] = dist[hi][wi] + 1
                q.append((nh, nw))

    if dist[h][w] == -1:
        print(-1)
        return

    print(h*w - b_cnt - dist[h][w] - 1)


if __name__ == '__main__':
    main()
