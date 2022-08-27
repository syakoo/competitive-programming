# 9min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ans = 0

    for i in range(1, n+1):
        if seek(i, 10) and seek(i, 8):
            ans += 1

    print(ans)


def seek(n: int, b: int) -> bool:
    while n > 0:
        r = n % b
        n = n // b
        if r == 7:
            return False

    return True


if __name__ == '__main__':
    main()
