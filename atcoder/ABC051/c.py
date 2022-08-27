
import math
import sys

sys.setrecursionlimit(10**6)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    sx, sy, tx, ty = map(int, input().split())
    cmds = []

    cmds.append('U'*(ty-sy))
    cmds.append('R'*(tx-sx))

    cmds.append('U')
    cmds.append('L'*(tx-(sx - 1)))
    cmds.append('D'*((ty + 1)-sy))
    cmds.append('R')

    cmds.append('R'*(tx-sx))
    cmds.append('U'*(ty-sy))

    cmds.append('R')
    cmds.append('D'*(ty-(sy - 1)))
    cmds.append('L'*((tx + 1)-sx))
    cmds.append('U')

    print(''.join(cmds))


if __name__ == '__main__':
    main()
