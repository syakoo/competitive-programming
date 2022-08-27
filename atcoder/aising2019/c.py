# 16 min
from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, map(int, input().split()))
    Sss = [input() for _ in range(h)]

    Xss = [[-1]*(w+2) for _ in range(h + 2)]
    for hi in range(h):
        for wi in range(w):
            Xss[hi + 1][wi + 1] = 1 if Sss[hi][wi] == '.' else 0

    used = [[0]*(w+2) for _ in range(h+2)]
    ans = 0
    for hi in range(1, h+1):
        for wi in range(1, w+1):
            if used[hi][wi]:
                continue

            used[hi][wi] = 1
            cnts = [0]*2
            cnts[Xss[hi][wi]] += 1
            q = deque([(hi, wi)])
            while q:
                hf, wf = q.popleft()

                for dh, dw in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    nh, nw = hf + dh, wf + dw
                    if not used[nh][nw] and Xss[nh][nw] == Xss[hf][wf] ^ 1:
                        used[nh][nw] = 1
                        cnts[Xss[nh][nw]] += 1
                        q.append((nh, nw))

            ans += cnts[0] * cnts[1]

    print(ans)


if __name__ == '__main__':
    main()
