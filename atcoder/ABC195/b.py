import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b, w = map(int, input().split())
    w *= 1000
    l = math.ceil(w/b)
    r = math.floor(w/a)
    if w < l or l > r:
        print('UNSATISFIABLE')
    else:
        print(l, r)


if __name__ == '__main__':
    main()
