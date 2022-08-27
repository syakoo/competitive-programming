def main():
    n = int(input())
    xs = set()

    for a in range(2, int(n**(1/2))+1):
        x = a * a
        while x <= n:
            xs.add(x)
            x *= a

    print(n - len(xs))


if __name__ == '__main__':
    main()
