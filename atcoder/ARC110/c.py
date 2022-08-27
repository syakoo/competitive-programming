# 39.33 min

def main():
    n = int(input())
    ps = list(map(int, input().split()))
    seek_num = 1
    anss = []

    for i in range(n-1):
        if ps[i+1] == seek_num:
            ps[i], ps[i+1] = ps[i+1], ps[i]
            anss += [j for j in range(i+1, seek_num - 1, -1)]
            seek_num = i + 2
            continue

        if ps[i] != i + 2:
            print(-1)
            return

    print("\n".join(str(ans) for ans in anss))


if __name__ == '__main__':
    main()
