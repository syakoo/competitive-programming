
def main():
    n, x, m = map(int, input().split())
    sums = []
    depths = [-1] * m

    su = x
    sums.append(x)
    depths[x] = 0
    loop = 1
    rloop = 0
    while loop < n:
        lx = x
        x = x**2 % m
        if depths[x] >= 0:
            su += (sums[depths[lx]] - sums[depths[x]] + x) * \
                ((n - loop)//(depths[lx] - depths[x] + 1))
            rloop = (n - loop) % (depths[lx] - depths[x] + 1)
            break
        else:
            depths[x] = loop
            su += x
            sums.append(su)
        loop += 1

    for _ in range(rloop):
        su += x
        x = x ** 2 % m

    print(su)


if __name__ == '__main__':
    main()
