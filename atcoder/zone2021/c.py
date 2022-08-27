import math
import sys
from collections import deque

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    q = deque([])
    rev = 0

    for si in s:
        if si == 'R':
            rev ^= 1
        else:
            if rev and len(q) > 0 and q[0] == si:
                q.popleft()
            elif rev == 0 and len(q) > 0 and q[-1] == si:
                q.pop()
            elif rev:
                q.appendleft(si)
            else:
                q.append(si)

    print(''.join(list(q)[::-1] if rev else list(q)))


if __name__ == '__main__':
    main()
