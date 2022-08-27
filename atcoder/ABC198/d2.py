
import math
from itertools import permutations


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s1 = input()
    s2 = input()
    s3 = input()

    chars = set()
    for s in s1+s2+s3:
        chars.add(s)

    idxes = dict()
    for i, char in enumerate(chars):
        idxes[char] = i

    siss = [lmap(lambda x: idxes[x], si) for si in (s1, s2, s3)]

    for digits in permutations(range(10), r=len(chars)):
        if digits[siss[0][0]] == 0 or digits[siss[1][0]] == 0 or digits[siss[2][0]] == 0:
            continue

        vs = [0] * 3
        for i, sis in enumerate(siss):
            for j, si in enumerate(sis):
                vs[i] += digits[si] * 10**(len(sis) - j - 1)

        v1, v2, v3 = vs
        if v1 + v2 == v3:
            print(v1, v2, v3, sep="\n")
            return

    print('UNSOLVABLE')
    return


if __name__ == '__main__':
    main()
