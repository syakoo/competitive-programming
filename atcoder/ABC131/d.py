<<<<<<< HEAD
import math
import sys

sys.setrecursionlimit(10**9)


=======
# 3 min
>>>>>>> 6ff60da37a54d105f7c01a9afebacd742500d696
def lmap(func, iter):
    return list(map(func, iter))


def main():
<<<<<<< HEAD
    pass
=======
    n = int(input())
    ABs = [lmap(int, input().split()) for _ in range(n)]

    ABs.sort(key=lambda ab: ab[1])
    t = 0
    for a, b in ABs:
        t += a
        if t > b:
            print("No")
            return

    print("Yes")
>>>>>>> 6ff60da37a54d105f7c01a9afebacd742500d696


if __name__ == '__main__':
    main()
