def main():
    h, w, n, m = map(int, input().split())
    ABs = [list(map(lambda x: int(x), input().split())) for _ in range(n)]
    CDs = [list(map(lambda x: int(x), input().split())) for _ in range(m)]
    lighted_dh = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
    lighted_dw = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
    M = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
    ans = 0

    for a, b in ABs:
        M[a][b] = 1
    for c, d in CDs:
        M[c][d] = -1

    for hi in range(1, h+1):
        for wi in range(1, w+1):
            if M[hi][wi] == -1:
                continue
            if lighted_dh[hi-1][wi] == 1:
                lighted_dh[hi][wi] = 1
            elif lighted_dh[hi-1][wi] == -1:
                lighted_dh[hi][wi] = -1
            else:
                for hj in range(hi, h+1):
                    if M[hj][wi] == -1:
                        lighted_dh[hi][wi] = -1
                        break
                    if M[hj][wi] == 1:
                        lighted_dh[hi][wi] = 1
                        break

    for hi in range(1, h+1):
        for wi in range(1, w+1):
            if M[hi][wi] == -1:
                continue
            if lighted_dw[hi][wi-1] == 1:
                lighted_dw[hi][wi] = 1
            elif lighted_dw[hi][wi-1] == -1:
                lighted_dw[hi][wi] = -1
            else:
                for wj in range(wi, w+1):
                    if M[hi][wj] == -1:
                        lighted_dw[hi][wi] = -1
                        break
                    if M[hi][wj] == 1:
                        lighted_dw[hi][wi] = 1
                        break

    for hi in range(1, h+1):
        for wi in range(1, w + 1):
            if lighted_dh[hi][wi] == 1 or lighted_dw[hi][wi] == 1:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
