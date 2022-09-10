import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))

def main():
    s = input()
    t = input()

    if len(s) > len(t):
        print('No')
        return
    
    if s == t[:len(s)]:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
