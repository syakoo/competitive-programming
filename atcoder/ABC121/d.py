# 44 min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b = map(int, input().split())

    def xors(x):
        b = 1 if (x // 2) % 2 == 1 else 0
        return 1 ^ b if x % 2 == 1 else x ^ b

    a = 0 if a == 0 else xors(a - 1)
    print(a ^ xors(b))


if __name__ == '__main__':
    main()
