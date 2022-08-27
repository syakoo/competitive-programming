import itertools


def main():
    n = int(input())
    XYs = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for p1, p2 in itertools.combinations(XYs, 2):
        if abs((p2[1] - p1[1]) / (p2[0] - p1[0])) <= 1:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
