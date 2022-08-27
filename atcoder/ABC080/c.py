
def lmap(func, iter):
    return list(map(func, iter))


def int2list(b: int) -> list:
    result = []
    while b > 0:
        result.append(b % 2)
        b //= 2

    return result


def main():
    n = int(input())
    Fss = [lmap(int, input().split()) for _ in range(n)]
    Pss = [lmap(int, input().split()) for _ in range(n)]
    ans = -10**9

    for b in range(1, 2 ** 10):
        bls = int2list(b)
        ans_b = 0

        for fs, ps in zip(Fss, Pss):
            cnt = 0
            for f, bl in zip(fs, bls):
                if f == bl == 1:
                    cnt += 1

            ans_b += ps[cnt]

        ans = max(ans, ans_b)

    print(ans)


if __name__ == '__main__':
    main()
