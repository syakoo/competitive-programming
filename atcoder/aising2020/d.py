def f(n: int) -> int:
    if n == 0:
        return 0
    cnt = 0
    x = n
    while x > 0:
        cnt += x & 1
        x >>= 1

    return f(n % cnt) + 1


def main():
    n = int(input())
    x = input()
    ones = x.count('1')

    a = int(x, 2)
    mod_p = a % (ones + 1)
    mod_n = a % (ones - 1) if ones > 1 else 0
    for i in range(n):
        if x[i] == '0':
            mod = pow(2, n-i-1, ones+1)
            mod = (mod + mod_p) % (ones + 1)
            print(f(mod) + 1)
        else:
            if ones == 1:
                print(0)
            else:
                mod = pow(2, n-i-1, ones-1)
                mod = (mod_n - mod) % (ones - 1)
                print(f(mod) + 1)


if __name__ == '__main__':
    main()
