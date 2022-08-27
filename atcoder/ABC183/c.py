import itertools


def main():
    n, k = map(int, input().split())
    Ts = [list(map(int, input().split())) for _ in range(n)]

    patterns = itertools.permutations(range(1, n))
    count = 0
    for p in patterns:
        su = Ts[0][p[0]] + Ts[0][p[-1]]
        for pi in range(len(p) - 1):
            su += Ts[p[pi]][p[pi+1]]

        if su == k:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
