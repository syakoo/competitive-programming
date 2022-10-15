from collections import deque


def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    Sss = [list(input()) for _ in range(h)]

    q = deque([(r - 1, c-1)])
    Sss[r-1][c-1] = 'o'
    while q:
        hi, wi = q.popleft()

        nh, nw = hi + 0, wi + 1
        if 0 <= nh < h and 0 <= nw < w and (Sss[nh][nw] == '.' or Sss[nh][nw] == '<'):
            q.append((nh, nw))
            Sss[nh][nw] = 'o'
        nh, nw = hi + 0, wi - 1
        if 0 <= nh < h and 0 <= nw < w and (Sss[nh][nw] == '.' or Sss[nh][nw] == '>'):
            q.append((nh, nw))
            Sss[nh][nw] = 'o'
        nh, nw = hi + 1, wi + 0
        if 0 <= nh < h and 0 <= nw < w and (Sss[nh][nw] == '.' or Sss[nh][nw] == '^'):
            q.append((nh, nw))
            Sss[nh][nw] = 'o'
        nh, nw = hi + -1, wi + 0
        if 0 <= nh < h and 0 <= nw < w and (Sss[nh][nw] == '.' or Sss[nh][nw] == 'v'):
            q.append((nh, nw))
            Sss[nh][nw] = 'o'

    for hi in range(h):
        for wi in range(w):
            if Sss[hi][wi] != '#' and Sss[hi][wi] != 'o':
                Sss[hi][wi] = 'x'

    for ss in Sss:
        print(''.join(ss))


if __name__ == '__main__':
    main()
