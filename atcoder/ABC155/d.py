# 無理くぼ
from bisect import bisect_right


def lmap(func, iter):
    return list(map(func, iter))


def cnt_lower(Xs: list, Ys: list, x: int) -> int:
    j = 0
    cnt = 0
    for i in range(len(Xs)):
        while j < len(Ys) and Xs[i]*Ys[j] <= x:
            j += 1
        cnt += j

    return cnt


def main():
    n, k = map(int, input().split())
    As = lmap(int, input().split())

    neg_cnt = 0
    zero_cnt = 0
    pos_cnt = 0
    Ngs = []
    Pos = []
    for a in As:
        if a == 0:
            zero_cnt += 1
        elif a > 0:
            pos_cnt += 1
            Pos.append(a)
        else:
            neg_cnt += 1
            Ngs.append(a)

    if neg_cnt*pos_cnt >= k:
        # neg
        Ngs.sort(reverse=True)
        Pos.sort(reverse=True)
        l, r = -10**18+1, 0
        while r - l > 1:
            m = (r + l)//2
            if cnt_lower(Ngs, Pos, m) > k:
                r = m
            else:
                l = m

        print(r)
    elif n*(n-1)//2 - pos_cnt*(pos_cnt-1)//2 >= k:
        print(0)
    else:
        # pos
        bias = n*(n-1)//2 - pos_cnt*(pos_cnt-1)//2
        print(bias)
        Pos.sort()
        reversed_Pos = Pos[::-1]
        l, r = 0, 10**18
        while r - l > 1:
            m = (r + l)//2
            pow_cnt = bisect_right(Pos, m**(0.5))
            print((cnt_lower(reversed_Pos, Pos, m) - pow_cnt)//2)
            if (cnt_lower(reversed_Pos, Pos, m) - pow_cnt)//2 + bias > k:
                r = m
            else:
                l = m

        print(r)
        print((cnt_lower(reversed_Pos, Pos, 448283280358331064) - pow_cnt)//2 + bias)


if __name__ == '__main__':
    main()
