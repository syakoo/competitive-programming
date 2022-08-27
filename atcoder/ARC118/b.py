def lmap(func, iter):
    return list(map(func, iter))


def pos_range(n: int, m: int, a: int, x: int):
    return (max(0, -(-(m*a - x)//n)), (m*a + x)//n)


def is_valid(n: int, m: int, As: list, x: int) -> bool:
    mn, mx = 0, 0
    for a in As:
        l, r = pos_range(n, m, a, x)

        mn += l
        mx += r

    return mn <= m <= mx


def main():
    k, n, m = map(int, input().split())
    As = lmap(int, input().split())

    l, r = -1, n*m
    while r - l > 1:
        mid = (r + l) // 2
        if is_valid(n, m, As, mid):
            r = mid
        else:
            l = mid

    err = r
    ranges = lmap(lambda a: pos_range(n, m, a, err), As)
    ans = lmap(lambda x: x[0], ranges)
    ans_sum = sum(ans)
    for i in range(k):
        add = min(ranges[i][1] - ranges[i][0], m - ans_sum)
        ans_sum += add
        ans[i] += add

    print(*ans)


if __name__ == '__main__':
    main()
