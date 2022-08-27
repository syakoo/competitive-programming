
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = input()
    st = ''

    nii = -1

    for ni in range(len(n) - 1, -1, -1):
        if n[ni] != '0':
            nii = ni + 1
            break
    st = n[:nii]

    for ni in range(len(st)//2 + 1):
        if st[ni] != st[-ni - 1]:
            print('No')
            return

    print('Yes')


if __name__ == '__main__':
    main()
