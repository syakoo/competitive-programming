# 13 min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    x, y, a, b, c = map(int, input().split())
    p = lmap(int, input().split())
    q = lmap(int, input().split())
    r = lmap(int, input().split())
    p.sort(reverse=True)
    q.sort(reverse=True)
    r.sort(reverse=True)

    aps = p[:x] + q[:y] + r[:min(x+y, c)]
    aps.sort(reverse=True)
    print(sum(aps[:(x+y)]))


if __name__ == '__main__':
    main()
