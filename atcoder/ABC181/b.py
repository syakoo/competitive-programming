# 3 min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ABs = [lmap(int, input().split()) for _ in range(n)]
    ans = 0

    for A, B in ABs:
        ans += B*(B+1) // 2 - A*(A-1)//2

    print(ans)


if __name__ == '__main__':
    main()
