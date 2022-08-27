# 9 min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())

    ans = 0
    subxor = 0
    r = 0
    for l in range(n):
        while r < n and As[r] ^ subxor == As[r] + subxor:
            subxor += As[r]
            r += 1

        ans += r - l
        subxor -= As[l]

    print(ans)


if __name__ == '__main__':
    main()
