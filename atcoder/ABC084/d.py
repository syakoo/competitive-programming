import itertools as it


def lmap(func, iter):
    return list(map(func, iter))


def is_prime(x: int) -> int:
    if x == 1:
        return False
    for y in range(2, int(x**(1/2))+1):
        if x % y == 0:
            return False

    return True


def main():
    q = int(input())
    LRs = [lmap(int, input().split()) for _ in range(q)]

    cnts = [0]*(10**5+1)
    for x in range(3, 10**5+1, 2):
        if is_prime(x) and is_prime((x + 1) // 2):
            cnts[x] += 1

    sumcnts = list(it.accumulate(cnts))
    for l, r in LRs:
        print(sumcnts[r] - sumcnts[l-1])


if __name__ == '__main__':
    main()
