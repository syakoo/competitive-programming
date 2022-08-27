# 8 min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, q = map(int, input().split())
    LRs = [lmap(int, input().split()) for _ in range(q)]
    counts = [0] * (n + 1)

    for l, r in LRs:
        counts[l - 1] += 1
        counts[r] -= 1

    for i in range(n):
        if i > 0:
            counts[i] = (counts[i] + counts[i - 1]) % 2
        else:
            counts[i] = counts[i] % 2

    print(''.join(str(c) for c in counts[:-1]))


if __name__ == '__main__':
    main()
