# 23 min
import math


def main():
    a, b, x = map(int, input().split())

    V = a*a*b
    if x*2 > V:
        S = (V - x)/a
        ans = math.degrees(math.atan(2*S/a**2))
    else:
        S = x / a
        ans = 90 - math.degrees(math.atan(2*S/b**2))

    print(ans)


if __name__ == '__main__':
    main()
