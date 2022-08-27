import math

def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    APXs = [lmap(int, input().split()) for _ in range(n)]
    ans = math.inf

    for a, p, x in APXs:
        if x - a - 0.5 > 0:
            ans = min(ans, p)

    if ans == math.inf:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
