
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = [int(input()) for _ in range(n)]
    cnts = [0] * (n + 1)

    for a in As:
        cnts[a] += 1

    x, y = 0, 0
    for i, a in enumerate(cnts):
        if a == 0:
            y = i
        elif a == 2:
            x = i

    if x == y == 0:
        print('Correct')
    else:
        print(x, y)


if __name__ == '__main__':
    main()
