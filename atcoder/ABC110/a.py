
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    ABC = lmap(int, input().split())
    ABC.sort()

    print(ABC[2]*10 + ABC[1] + ABC[0])


if __name__ == '__main__':
    main()
