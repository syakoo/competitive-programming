import math


def main():
    n = int(input())
    A = list(map(int, input().split()))
    pre_ans = max(0, A[0])
    ans = max(0, A[0])
    i_sum = A[0]
    pre_sum = A[0]
    pre_sum_mx = A[0]
    sm = A[0]

    for i in range(1, n):
        ans = max(ans, sm+pre_sum_mx, sm + pre_sum + A[i])
        if ans != pre_ans:
            i_sum = 0
        i_sum += sm + A[i]
        pre_sum = pre_sum + A[i]
        pre_sum_mx = max(pre_sum, pre_sum_mx)
        sm += pre_sum

    print(ans)


if __name__ == '__main__':
    main()
