from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    Sss = [input() for _ in range(h)]

    ans = [['x' for _ in range(w)] for _ in range(h)]
    ans[r-1][c-1] = 'o'
    q = deque([(r-1, c-1)])
    while q:
        hi, wi = q.popleft()

        # >
        if 0 <= wi - 1 < w and Sss[hi][wi-1] in '.>' and ans[hi][wi-1] != 'o':
            ans[hi][wi-1] = 'o'
            q.append((hi, wi-1))
        # <
        if 0 <= wi + 1 < w and Sss[hi][wi+1] in '.<' and ans[hi][wi+1] != 'o':
            ans[hi][wi+1] = 'o'
            q.append((hi, wi+1))
        # ^
        if 0 <= hi - 1 < h and Sss[hi-1][wi] in '.v' and ans[hi-1][wi] != 'o':
            ans[hi-1][wi] = 'o'
            q.append((hi-1, wi))
        # v
        if 0 <= hi + 1 < h and Sss[hi+1][wi] in '.^' and ans[hi+1][wi] != 'o':
            ans[hi+1][wi] = 'o'
            q.append((hi+1, wi))

    for hi in range(h):
        for wi in range(w):
            if Sss[hi][wi] == '#':
                ans[hi][wi] = '#'

    print('\n'.join(''.join(row) for row in ans))


if __name__ == '__main__':
    main()
