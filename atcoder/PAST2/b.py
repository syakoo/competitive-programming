
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    a_cnts = s.count('a')
    b_cnts = s.count('b')
    c_cnts = s.count('c')

    mx_cnts = max(a_cnts, b_cnts, c_cnts)
    if a_cnts == mx_cnts:
        print('a')
    elif b_cnts == mx_cnts:
        print('b')
    else:
        print('c')

if __name__ == '__main__':
    main()
