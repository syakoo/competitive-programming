
def main():
    x, y, a, b = map(int, input().split())
    ex = 0
    while x*a < x + b and x < y:
        x *= a
        ex += 1

    print((y - x)//b + bool((y - x) % b) - 1 + ex)


if __name__ == '__main__':
    main()
