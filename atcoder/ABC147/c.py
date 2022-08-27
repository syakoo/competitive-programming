# 23 min

def lmap(func, iter):
    return list(map(func, iter))


def is_valid(AXYs: list, b: list):
    n = len(AXYs)
    for ai in range(n):
        if not b & (1 << ai):
            continue

        for x, y in AXYs[ai]:
            x -= 1
            if y == 0 and b & (1 << x):
                return False
            elif y == 1 and not b & (1 << x):
                return False

    return True


def main():
    n = int(input())
    AXYs = [[] for _ in range(n)]

    for i in range(n):
        a = int(input())
        AXYs[i] = [lmap(int, input().split()) for _ in range(a)]

    ans = 0
    for b in range(1 << n):
        if is_valid(AXYs, b):
            cnt = 0
            for i in range(n):
                if b & (1 << i):
                    cnt += 1

            ans = max(ans, cnt)

    print(ans)


if __name__ == '__main__':
    main()
