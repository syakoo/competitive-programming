import math


def main():
    a, b, h, m = map(int, input().split())

    print(math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(((h+m/60)/12-m/60)*360))))


if __name__ == '__main__':
    main()
