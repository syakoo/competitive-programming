from collections import Counter


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())

    Bs = [0]
    for i, a in enumerate(As):
        Bs.append(a*((-1)**i) + Bs[-1])

    cnts = Counter(Bs)
    ans = 0
    for _, v in cnts.items():
        ans += v*(v-1) // 2

    print(ans)


if __name__ == '__main__':
    main()
