
def main():
    n = int(input())
    l, r = 0, 10**18
    while r - l > 1:
        m = (r+l)//2
        if m*(m+1)//2 <= n+1:
            l = m
        else:
            r = m

    print(n - l + 1)


if __name__ == '__main__':
    main()
