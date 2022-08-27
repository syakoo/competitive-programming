
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    IABs = [[i] + list(map(int, input().split())) for i in range(n)]

    IABs_a = sorted(IABs, key=lambda x: x[1])
    IABs_b = sorted(IABs, key=lambda x: x[2])

    if IABs_a[0][0] == IABs_b[0][0]:
        print(min(IABs_a[0][1] + IABs_b[0][2],
                  max(IABs_a[0][1], IABs_b[1][2]), max(IABs_a[1][1], IABs_b[0][2])))
    else:
        print(max(IABs_a[0][1], IABs_b[0][2]))


if __name__ == '__main__':
    main()
