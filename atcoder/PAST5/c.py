def main():
    n = int(input())
    s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans = []

    if n == 0:
        print(0)
        return

    while n > 0:
        q, r = divmod(n, 36)
        ans.append(s[r])
        n = q

    print(''.join(reversed(ans)))


if __name__ == '__main__':
    main()
