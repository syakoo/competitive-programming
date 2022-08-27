import itertools


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m, q = map(int, input().split())
    ABCDs = [lmap(int, input().split()) for _ in range(q)]
    ans = 0

    for As in itertools.combinations_with_replacement(range(1, m+1), n):
        value = 0
        for a, b, c, d in ABCDs:
            if As[b-1] - As[a - 1] == c:
                value += d

        ans = max(value, ans)

    print(ans)


if __name__ == '__main__':
    main()
