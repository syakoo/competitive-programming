import math


def main():
    A = list(map(int, input().split()))
    E = [[[0 for _ in range(100)] for _ in range(100)]for _ in range(100)]

    def find(Ad, d):
        if Ad == [99, 99, 99]:
            return d + 1
        if E[Ad[0]][Ad[1]][Ad[2]] != 0:
            return E[Ad[0]][Ad[1]][Ad[2]]

        Ed = 0
        for i in range(3):
            if (Ad[i] == 99):
                Ed += (Ad[i] / (Ad[0] + Ad[1] + Ad[2])) * (d+1)
                continue

            ne_Ad = Ad[:]
            ne_Ad[i] += 1
            ne_edi = (Ad[i] / (Ad[0] + Ad[1] + Ad[2])) * find(ne_Ad, d + 1)
            Ed += ne_edi

        E[Ad[0]][Ad[1]][Ad[2]] = Ed
        return Ed

    print(find(A, 0))


if __name__ == '__main__':
    main()
