def sum_seq(x): return (x * (x + 1)) / 2


def bisect(l: int, r: int, n: int) -> int:
    if r - l < 1:
        if sum_seq(r) > n:
            return l - 1
        else:
            return r

    p = (r - l) // 2 + l
    sum_p = sum_seq(p)
    if sum_p == n:
        return p
    elif sum_p > n:
        return bisect(l, p - 1, n)
    else:
        return bisect(p + 1, r, n)


def main():
    n = int(input())
    a = bisect(0, n, n + 1)

    print(a)
    print(n - a + 1)


if __name__ == '__main__':
    main()
