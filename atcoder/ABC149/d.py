# 9 min
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()

    points = {'r': p, 's': r, 'p': s}
    ans = sum(points[ti] for ti in t[:k])
    xs = [True]*k + [False]*(n-k)
    for i in range(k, n):
        if xs[i-k] and t[i] == t[i-k]:
            continue

        xs[i] = True
        ans += points[t[i]]

    print(ans)


if __name__ == '__main__':
    main()
