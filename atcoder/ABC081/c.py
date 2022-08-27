from collections import Counter


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())

    cnts = Counter(As)
    ans = 0
    flg = False
    for v, c in sorted(cnts.items(), reverse=True):
        if c >= 2:
            if ans == 0:
                ans = v
                if c >= 4:
                    ans = v*v
                    flg = True
                    break
            else:
                ans *= v
                flg = True
                break

    if flg:
        print(ans)
    else:
        print(0)


if __name__ == '__main__':
    main()
