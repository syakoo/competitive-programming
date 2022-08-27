
def main():
    n = int(input())
    ABs = [list(map(int, input().split())) for _ in range(n)]

    ABs.sort(key=lambda p: 2*p[0] + p[1], reverse=True)
    num = sum(map(lambda p: -p[0], ABs))
    ans = 0

    for a, b in ABs:
        ans += 1
        num += 2*a + b
        if num > 0:
            print(ans)
            return


if __name__ == '__main__':
    main()
