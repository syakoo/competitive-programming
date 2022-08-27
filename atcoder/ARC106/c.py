# 52 min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    if m < 0 or m == n:
        print(-1)
        return
    if m == n - 1 and n >= 2:
        print(-1)
        return

    LRs = lmap(lambda i: (3*i + 2, 3*i + 3), range(n - 1))
    if m == 0:
        LRs.append((3*(n - 1) + 2, 3*(n - 1) + 3))
    else:
        LRs.append((1, 3*(m + 1) + 1))

    print('\n'.join(f'{l} {r}' for l, r in LRs))


if __name__ == '__main__':
    main()
