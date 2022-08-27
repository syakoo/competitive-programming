from collections import Counter


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Ds = lmap(int, input().split())
    m = int(input())
    Ts = lmap(int, input().split())

    dcnts = Counter(Ds)
    for t in Ts:
        if t in dcnts and dcnts[t] > 0:
            dcnts[t] -= 1
        else:
            print('NO')
            return

    print('YES')


if __name__ == '__main__':
    main()
