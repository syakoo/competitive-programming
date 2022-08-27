import math


def main():
    h, w, n, m = map(int, input().split())
    cols = [[0 for _ in range(w)] for _ in range(h)]
    rows = [[0 for _ in range(w)] for _ in range(h)]

    lights = [list(map(lambda x: int(x) - 1, input().split()))
              for _ in range(n)]

    for _ in range(m):
        x, y = map(lambda x: int(x) - 1, input().split())
        rows[y][x] = "B"
        cols[y][x] = "B"

    for li in lights:
        x, y = li
        while x > 0 and rows[y][x-1] == 0:
            rows[y][x-1] = True
            x -= 1
        x, y = li
        while x < w and rows[y][x] == 0:
            rows[y][x] = True
            x += 1
        x, y = li
        while y > 0 and cols[y-1][x] == 0:
            cols[y-1][x] = True
            y -= 1
        x, y = li
        while y < h and cols[y][x] == 0:
            cols[y][x] = True
            y += 1
    count = 0
    for hi in range(h):
        for wi in range(w):
            if rows[hi][wi] == True or cols[hi][wi] == True:
                count += 1

    print(count)


if __name__ == '__main__':
    main()
