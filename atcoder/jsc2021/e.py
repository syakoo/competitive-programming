
import math


def lmap(func, iter):
    return list(map(func, iter))


def make_perf_tree(s):
    sn = len(s)
    if sn == 1:
        return s

    sp = ''
    if not sn & 1:
        sp = 'e'
    return sp.join([make_perf_tree(s[:sn//2]), make_perf_tree(s[sn//2:])])


def main():
    k = int(input())
    s = input()
    sn = len(s)

    if k == 0:
        print('impossible')

    if sn == 1:
        print(0)
        return

    s = make_perf_tree(s)
    sn = len(s)
    mx_lv = int(math.log2(sn) + 1)

    if k > mx_lv or k == mx_lv - 1:
        print('impossible')
        return

    leaven = 2**(mx_lv - k) - 1
    leaves = []
    for i in range(0, sn, leaven + 1):
        leaves.append(s[i:i + leaven])

    print(leaves)


if __name__ == '__main__':
    main()
