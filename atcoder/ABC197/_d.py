from numpy import sin, cos, array, pi


def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x, y = map(int, input().split())
    theta = (pi * 2) / n
    xc, yc = (x + x0) / 2, (y + y0) / 2

    rotate = array([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]])

    x1, y1 = (rotate @ array([x0-xc, y0-yc])) + array([xc, yc])
    print(x1, y1)


if __name__ == "__main__":
    main()
