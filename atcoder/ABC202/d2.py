def main():
    a, b, k = map(int, input().split())

    cmbss = [[0]*(a + 1) for _ in range(a + b + 1)]
    cmbss[0][0] = 1
    for n in range(1, a + b + 1):
        for ai in range(a + 1):
            cmbss[n][ai] += cmbss[n - 1][ai]
            if ai > 0:
                cmbss[n][ai] += cmbss[n - 1][ai - 1]

    ans = []
    ab = a + b
    for _ in range(ab):
        if cmbss[a + b - 1][a - 1] < k or a == 0:
            ans.append('b')
            k -= cmbss[a + b - 1][a - 1]
            b -= 1
        else:
            ans.append('a')
            a -= 1

    print(''.join(ans))


if __name__ == '__main__':
    main()
