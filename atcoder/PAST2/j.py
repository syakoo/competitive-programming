
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    stack = []
    x = ''

    for si in s:
        if si == '(':
            stack.append(x)
            x = ''
        elif si == ')':
            x2 = x + x[::-1]
            x = stack.pop()
            x += x2
        else:
            x += si

    print(x)


if __name__ == '__main__':
    main()
