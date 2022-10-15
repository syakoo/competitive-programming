import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    x = int(input())

    cs = ['']
    cnts = [0]
    c = []
    cnt = 0
    for si in s:
        if si in '123456789':
            cs.append(''.join(c))
            cnt *= int(si) + 1
            cnts.append(cnt)
            c = []
        else:
            cnt += 1
            c.append(si)

        if cnt > 10**15:
            break

    if c:
        cs.append(''.join(c))
        cnts.append(cnt)

    x -= 1
    for i in reversed(range(len(cs))):
        x = x % (cnts[i - 1] + len(cs[i]))

        if x >= cnts[i - 1]:
            print(cs[i][x - cnts[i-1]])
            return


if __name__ == '__main__':
    main()
