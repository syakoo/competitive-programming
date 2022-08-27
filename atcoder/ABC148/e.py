
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())

    if n % 2 == 1:
        print(0)
        return

    a = 10
    ans = 0
    while n >= a:
        ans += n // a
        a *= 5

    print(ans)


if __name__ == '__main__':
    main()
