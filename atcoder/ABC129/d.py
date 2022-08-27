# 13 min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    Sss = [input() for _ in range(h)]
    hSss = [[0 for _ in range(w)] for _ in range(h)]
    wSss = [[0 for _ in range(w)] for _ in range(h)]

    for hi in range(h):
        for wi in range(w):
            if Sss[hi][wi] == '#':
                continue
            if wi == 0 or Sss[hi][wi - 1] == '#':
                wj = wi
                while wj < w and Sss[hi][wj] == '.':
                    wj += 1
                wSss[hi][wi] = wj - wi
            else:
                wSss[hi][wi] = wSss[hi][wi - 1]

    for hi in range(h):
        for wi in range(w):
            if Sss[hi][wi] == '#':
                continue
            if hi == 0 or Sss[hi - 1][wi] == '#':
                hj = hi
                while hj < h and Sss[hj][wi] == '.':
                    hj += 1
                hSss[hi][wi] = hj - hi
            else:
                hSss[hi][wi] = hSss[hi - 1][wi]

    ans = 0

    for hi in range(h):
        for wi in range(w):
            ans = max(ans, hSss[hi][wi] + wSss[hi][wi] - 1)

    print(ans)


if __name__ == '__main__':
    main()
