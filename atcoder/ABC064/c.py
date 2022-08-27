def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())

    cnt = 0
    colors = set()
    for a in As:
        if a >= 3200:
            cnt += 1
        else:
            colors.add(a//400)

    print(max(1, len(colors)), len(colors) + cnt)


if __name__ == '__main__':
    main()
