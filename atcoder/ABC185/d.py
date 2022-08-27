import math


def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if m == 0:
        print(1)
        return

    difA = []
    if A[0] - 1 > 0:
        difA.append(A[0] - 1)
    if n-A[-1] > 0:
        difA.append(n-A[-1])
    for ai in range(m - 1):
        difa = A[ai + 1] - A[ai] - 1
        if difa > 0:
            difA.append(difa)
    if not difA:
        print(0)
        return

    ans = 0
    min_dif = min(difA)
    for difa in difA:
        ans += math.ceil(difa / min_dif)

    print(ans)


if __name__ == '__main__':
    main()
