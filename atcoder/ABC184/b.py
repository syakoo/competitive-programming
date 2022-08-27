import math


def main():
    n, x = map(int, input().split())
    s = input()

    for si in s:
        if si == 'x' and x > 0:
            x -= 1
        elif si == 'o':
            x += 1

    print(x)


if __name__ == '__main__':
    main()
