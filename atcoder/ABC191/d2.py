RATIO = 10000


def toZ(cs: str) -> int:
    if '.' not in cs:
        return int(cs)*RATIO
    xs, ys = cs.split('.')
    return int(xs + (ys + '0000')[:4])


def main():
    ratio = RATIO
    x, y, r = map(toZ, input().split())

    xl = -(-(x - r)//ratio)*ratio
    xr = ((x + r)//ratio)*ratio
    ans = 0
    for xi in range(xl, xr+1, ratio):
        yr = y + (r**2 - (xi - x)**2)**.5
        yl = y - (r**2 - (xi - x)**2)**.5

        for yi in range(int(yr)//ratio+2, int(yr)//ratio-3, -1):
            if (yi*ratio - y)**2 + (xi - x)**2 <= r**2:
                ans += yi
                break
        for yi in range(int(yl)//ratio+2, int(yl)//ratio-3, -1):
            if yi*ratio < y and (yi*ratio - y)**2 + (xi - x)**2 > r**2:
                ans -= yi
                break

    print(ans)


if __name__ == '__main__':
    main()
