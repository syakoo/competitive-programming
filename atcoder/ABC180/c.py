import math


def main():
    n = int(input())
    anses = set()

    for i in range(1, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            anses.add(i)
            anses.add(n // i)
    anses = list(anses)
    anses.sort()

    for i in anses:
        print(i)


if __name__ == '__main__':
    main()
