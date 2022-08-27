
def main():
    n = int(input())
    com = 0

    for _ in range(n):
        d1, d2 = map(int, input().split())

        if d1 == d2:
            com += 1
        else:
            com = 0

        if com == 3:
            print('Yes')
            return

    print('No')


if __name__ == '__main__':
    main()
