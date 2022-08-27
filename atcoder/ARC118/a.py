import math


def main():
    t, n = map(int, input().split())
    print(math.ceil(100*n/t) + n - 1)


if __name__ == '__main__':
    main()
