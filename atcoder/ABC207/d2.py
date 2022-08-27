import math


def lmap(func, iter):
    return list(map(func, iter))


def is_same(ABs: list, CDs: list) -> bool:
    ABs.sort()
    CDs.sort()
    dx = CDs[0][0] - ABs[0][0]
    dy = CDs[0][1] - ABs[0][1]

    ABs = lmap(lambda ab: [ab[0] + dx, ab[1] + dy], ABs)
    e = 10**(-3)
    for ab, cd in zip(ABs, CDs):
        if abs(ab[0] - cd[0]) + abs(ab[1] - cd[1]) > e:
            return False

    return True


def main():
    n = int(input())
    ABs = [lmap(int, input().split()) for _ in range(n)]
    CDs = [lmap(int, input().split()) for _ in range(n)]

    for deg in range(3600):
        rad = math.radians(deg*0.1)
        AB2s = lmap(lambda ab: (
            ab[0]*math.cos(rad) - ab[1]*math.sin(rad),
            ab[0]*math.sin(rad) + ab[1]*math.cos(rad)
        ), ABs[:])

        if is_same(AB2s, CDs):
            print('Yes')
            return
    print('No')


if __name__ == '__main__':
    main()
