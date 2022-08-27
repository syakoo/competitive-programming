from math import gcd


def lcm(n: int, m: int) -> int:
    return n*m // gcd(n, m)


def cnt_division(n: int, m: int, x: int) -> int:
    return m//x - (n-1)//x


def main():
    # input
    A, B, C, D = map(int, input().split())

    # compute
    cnt_all = B - A + 1
    cnt_c = cnt_division(A, B, C)
    cnt_d = cnt_division(A, B, D)
    cnt_cd = cnt_division(A, B, lcm(C, D))

    # output
    print(cnt_all-cnt_c-cnt_d+cnt_cd)


if __name__ == '__main__':
    main()
