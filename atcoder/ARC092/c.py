def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ABs = [lmap(int, input().split()) for _ in range(n)]
    CDs = [lmap(int, input().split()) for _ in range(n)]

    ABs.sort()
    CDs.sort()
    for c, d in CDs:
        mx_i = -1
        for i, (a, b) in enumerate(ABs):
            if a >= c:
                break
            if b < d:
                if mx_i == -1 or b > ABs[mx_i][1]:
                    mx_i = i

        if mx_i != -1:
            ABs.pop(mx_i)

    print(n - len(ABs))


if __name__ == '__main__':
    main()
