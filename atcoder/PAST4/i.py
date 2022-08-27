
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    sumA = sum(As)
    As += As
    r = 0
    dAs = 0
    ans = sumA

    for l in range(n):
        while (r - l) <= 0 or (r - l < n - 1 and sumA > 2*dAs):
            dAs += As[r]
            r += 1

        if r - l == 0:
            ans = min(ans, abs(sumA - 2*dAs))
        else:
            ans = min(ans, abs(sumA - 2*dAs), abs(sumA - 2*(dAs - As[r])))
        dAs -= As[l]

    print(ans)


if __name__ == '__main__':
    main()
