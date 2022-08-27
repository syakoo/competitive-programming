
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Cs = input()
    ans = 0
    R_cnt = Cs.count('R')

    for i in range(R_cnt):
        if Cs[i] == 'W':
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
