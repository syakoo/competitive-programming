# 13 min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b, c = map(int, input().split())
    ps = []
    x = a % 10

    while x not in ps:
        ps.append(x)
        x = (x * a) % 10

    pn = len(ps)

    print(ps[(pow(b, c, pn) - 1) % pn])


if __name__ == '__main__':
    main()
