
def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b, x = map(int, input().split())
    l, r = 0, 10**9
    def value(n): return a*n + b*len(str(n))

    while r - l > 1:
        n = (r + l)//2
        if value(n) > x:
            r = n
        else:
            l = n

    print(l if value(r) > x else r)


if __name__ == '__main__':
    main()
