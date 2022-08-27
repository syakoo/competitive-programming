import math


def main():
    ni = list(map(lambda x: int(x) % 3, input()))
    sum_ni = sum(ni) % 3

    if sum_ni == 0:
        return 0
    elif len(ni) == 1:
        return -1
    elif sum_ni == 1 and 1 in ni:
        return 1
    elif sum_ni == 2 and 2 in ni:
        return 1

    if len(ni) <= 2:
        return -1

    return 2


if __name__ == '__main__':
    print(main())
