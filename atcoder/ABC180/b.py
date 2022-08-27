import math


def main():
    n = int(input())
    xs = list(map(int, input().split()))

    print(sum([abs(x) for x in xs]))
    print(math.sqrt(sum([x * x for x in xs])))
    print(max([abs(x) for x in xs]))


if __name__ == '__main__':
    main()
