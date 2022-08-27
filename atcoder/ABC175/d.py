
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    Ps = lmap(int, input().split())
    Cs = lmap(int, input().split())
    Ps = lmap(lambda x: x-1, Ps)

    colors = [0]*n
    cycless = []
    color = 1
    for i in range(n):
        if colors[i]:
            continue

        cycles = [Cs[i]]
        colors[i] = color
        pos = i
        while True:
            pos = Ps[pos]
            if colors[pos]:
                break
            colors[pos] = color
            cycles.append(Cs[pos])

        cycless.append(cycles)
        color += 1

    ans = -1 << 60
    for cycles in cycless:
        loop = sum(cycles)
        cyclen = len(cycles)
        r = k % cyclen
        for i in range(cyclen):
            point = 0
            for j in range(min(cyclen, k)):
                point += cycles[(i+j) % cyclen]
                ans = max(ans, point)
                if k > cyclen:
                    ans = max(ans, loop*(k//cyclen-1)+point)
                if j < r:
                    ans = max(ans, loop*(k//cyclen)+point)

    print(ans)


if __name__ == '__main__':
    main()
