# 18 min
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    S = input()

    cnts = []
    cnt = 0
    s = '#'
    for si in S:
        if s == si:
            cnt += 1
        else:
            cnts.append(cnt)
            s = si
            cnt = 1
    cnts.append(cnt)

    if S[0] != '0':
        cnts = cnts[1:]
    if S[-1] == '0':
        cnts += [0]

    n = len(cnts)
    if n <= 2*k+1:
        print(sum(cnts))
        return

    score = sum(cnts[:2*k+1])
    mx = score
    for l in range(0, n-2*k-2, 2):
        r = l + 2*k + 1
        score += cnts[r] + cnts[r+1] - cnts[l] - cnts[l+1]
        mx = max(mx, score)

    print(mx)


if __name__ == '__main__':
    main()
