# 18min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    As.sort(reverse=True)
    ans = 0

    for i, ai in enumerate(As):
        x = n - (i + 1)
        y = i
        ans += ai * (x - y)

    print(ans)


if __name__ == '__main__':
    main()
