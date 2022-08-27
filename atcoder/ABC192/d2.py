def check(x: str, m: int, n: int) -> bool:
    v = 0

    for i, xi in enumerate(x):
        v += int(xi)*(n**(len(x)-i-1))
        if v > m:
            return False

    return True


def main():
    x = input()
    x_list = [int(xi) for xi in x]
    m = int(input())
    d = max(x_list)

    if len(x) == 1:
        if int(x) <= m:
            print(1)
            return
        else:
            print(0)
            return

    l_idx, r_idx = 1, m+1
    while r_idx - l_idx > 1:
        n = (r_idx + l_idx)//2
        if check(x, m, n):
            l_idx = n
        else:
            r_idx = n

    print(max(0, l_idx - d))


if __name__ == '__main__':
    main()
