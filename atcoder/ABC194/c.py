
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    sqAs = lmap(lambda x: x**2, As)
    suAs = [0] * n

    for i in range(n-1, -1, -1):
        if i == n-1:
            suAs[i] = As[i]
        else:
            suAs[i] = As[i] + suAs[i + 1]

    ans = (n - 1)*sum(sqAs)

    for i in range(n-1):
        ans -= 2*As[i]*suAs[i + 1]

    print(ans)


if __name__ == '__main__':
    main()
