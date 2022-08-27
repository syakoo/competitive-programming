import math


def lmap(func, iter):
    return list(map(func, iter))


def f(a: int, b: int, x: int) -> int:
    return b//x - (a-1)//x


def main():
    a, b, c, d = map(int, input().split())

    cd = c*d//math.gcd(c, d)

    print(b-a+1-(f(a, b, c) + f(a, b, d) - f(a, b, cd)))


if __name__ == '__main__':
    main()
