
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())

    scanAs = [0]*(n + 1)
    scanAs[-1] = As[-1]
    for i in range(n-1, -1, -1):
        scanAs[i] = scanAs[i+1] + As[i]

    ans = 1
    nodes = 1 - As[0]
    for i in range(1, n+1):
        ni = min(nodes*2, scanAs[i])
        ans += ni
        nodes += nodes - As[i]
        if nodes < 0:
            print(-1)
            return

    if nodes < 0:
        print(-1)
        return
    print(ans)


if __name__ == '__main__':
    main()
