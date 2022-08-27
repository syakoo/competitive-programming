def main():
    n = int(input())

    idxs = ['Male', 'Female']
    print(0)
    b = input()
    if b == 'Vacant':
        return
    elif b == 'Female':
        idxs = idxs[::-1]

    l, r = 0, n-1
    while r - l > 1:
        m = (r + l) // 2
        print(m)
        s = input()
        if s == 'Vacant':
            return
        elif idxs.index(s) == m % 2:
            l = m
        else:
            r = m

    print(r)


if __name__ == '__main__':
    main()
