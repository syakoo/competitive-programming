# 10 min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    xys = [lmap(int, input().split()) for _ in range(n)]
    lines = set()

    for i in range(n-1):
        for j in range(i+1, n):
            x1, y1 = xys[i]
            x2, y2 = xys[j]
            if x1 != x2:
                a = (y2 - y1) / (x2 - x1)
                b = y1 - a * x1
            else:
                a = x1
                b = None

            if (a, b) in lines:
                print("Yes")
                return

            lines.add((a, b))

    print("No")


if __name__ == '__main__':
    main()
