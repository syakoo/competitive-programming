import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ABs = [lmap(int, input().split()) for _ in range(n)]

    Ls, Rs = lmap(lambda x: x[0], ABs), lmap(lambda x: x[1], ABs)
    Ls.sort()
    Rs.sort(reverse=True)
    if n % 2:
        mid = math.ceil(n / 2) - 1
        print(Rs[mid] - Ls[mid] + 1)
    else:
        mid = math.ceil(n / 2) - 1
        r = (Rs[mid] + Rs[mid+1]) / 2
        l = (Ls[mid] + Ls[mid+1]) / 2
        print(int((r - l) * 2) + 1)


if __name__ == '__main__':
    main()
