
def main():
    n = int(input())
    As = list(map(int, input().split()))
    ans = 1
    if 0 in As:
        print(0)
        return

    for a in As:
        ans *= a
        if ans > 10**18:
            print(-1)
            return

    print(ans)


if __name__ == '__main__':
    main()
