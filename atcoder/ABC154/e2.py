from functools import lru_cache


@lru_cache(None)
def f(x: int, k: int) -> int:
    assert x >= 0

    if x < 10:
        if k == 1:
            return x
        elif k == 0:
            return 1

        return 0

    m, r = divmod(x, 10)
    cnt = 0
    if k > 0:
        cnt += r * f(m, k-1)
        cnt += (9 - r) * f(m-1, k-1)

    cnt += f(m, k)
    return cnt


def main():
    n = int(input())
    k = int(input())
    print(f(n, k))


main()
