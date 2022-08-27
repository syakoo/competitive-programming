from itertools import accumulate


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = [0] + lmap(int, input().split()) + [0]

    dists = lmap(lambda aa: abs(aa[0] - aa[1]), zip(As, As[1:]))
    ls = [0] + list(accumulate(dists))
    rs = list(accumulate(reversed(dists)))[::-1] + [0]

    for i in range(n):
        res = ls[i] + abs(As[i] - As[i+2]) + rs[i+2]
        print(res)


if __name__ == '__main__':
    main()
