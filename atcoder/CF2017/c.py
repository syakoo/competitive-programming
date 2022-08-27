# 23 min

import math
import sys
from collections import Counter

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    Ass = [input() for _ in range(h)]
    cnts = Counter(''.join(Ass))
    odd_cnt = 0
    double_cnt = 0
    for cnt in cnts.values():
        if cnt % 2:
            odd_cnt += 1
            cnt -= 1
        if cnt % 4 != 0:
            double_cnt += 1

    if h % 2 and w % 2:
        if odd_cnt == 1 and double_cnt <= (h + w - 2) // 2:
            print('Yes')
            return
    elif h % 2:
        if odd_cnt == 0 and double_cnt <= w // 2:
            print('Yes')
            return
    elif w % 2:
        if odd_cnt == 0 and double_cnt <= h // 2:
            print('Yes')
            return
    else:
        if odd_cnt + double_cnt == 0:
            print('Yes')
            return

    print('No')


if __name__ == '__main__':
    main()
