# 20 min
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())

    As.sort(reverse=True)
    sumAs = [0]
    for a in As:
        sumAs.append(sumAs[-1]+a)

    ans = 1 << 60
    for i in range(n):
        x = As[i]/2
        res = sumAs[i] - i*x + (n-i)*x
        ans = min(ans, res)

    print(ans/n)


if __name__ == '__main__':
    main()
