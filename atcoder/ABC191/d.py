# not cleared
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    x, y, r = map(float, input().split())
    xrange = range(math.ceil(x - r), math.floor(x + r) + 1)
    ans = 0

    for xi in xrange:
        t = math.sqrt(r**2 - (x - xi)**2)
        print(xi, y-t, y+t)
        # ans += math.floor(y + t) - math.ceil(y - t)
        ans += len(range(math.ceil(y - t), math.floor(y + t) + 1))

    print(ans)


if __name__ == '__main__':
    main()
