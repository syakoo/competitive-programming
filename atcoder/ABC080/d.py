def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, C = map(int, input().split())
    STCs = [lmap(int, input().split()) for _ in range(n)]
    tmx = max(map(lambda x: x[1], STCs))

    channels = [[0]*C for _ in range(tmx+2)]
    for s, t, c in STCs:
        channels[s][c-1] += 1
        channels[t][c-1] += -1

    ans = 0
    for i in range(tmx+1):
        for ci in range(C):
            channels[i+1][ci] += channels[i][ci]

        cnt = sum(map(lambda x: x[0] | x[1], zip(channels[i], channels[i+1])))
        ans = max(ans, cnt)

    print(ans)


if __name__ == '__main__':
    main()
