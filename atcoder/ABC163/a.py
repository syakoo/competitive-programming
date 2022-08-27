import math

def lmap(func, iter):
    return list(map(func, iter))


def main():
    r = int(input())
    print(2*r*math.pi)


if __name__ == '__main__':
    main()

