import math


def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0

    mx = max(A)
    mx_num = 0
    for i in range(2, mx + 1):
        num = 0
        for a in A:
            if a % i == 0:
                num += 1
        if mx_num < num:
            mx_num = num
            ans = i

    print(ans)


if __name__ == '__main__':
    main()
