
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s, t = input().split()
    els = ["B9", "B8", "B7", "B6", "B5", "B4", "B3", "B2", "B1",
           "1F", "2F", "3F", "4F", "5F", "6F", "7F", "8F", "9F"]

    print(abs(els.index(s) - els.index(t)))


if __name__ == '__main__':
    main()
