from itertools import product


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    ABCs = [lmap(int, input().split()) for _ in range(m)]

    ans = 0
    for indices in product([0, 1], repeat=n):
        flg = False
        xs = [0]*n
        for a, b, c in ABCs:
            abc = lmap(lambda x: indices[x-1], (a, b, c))
            if abc == [1, 1, 1]:
                flg = True
                break
            if abc.count(1) == 2:
                i = abc.index(0)
                xs[[a, b, c][i]-1] = 1

        if flg or any(i == x == 0 for i, x in zip(indices, xs)):
            continue

        ans = max(ans, indices.count(0))

    print(ans)


if __name__ == '__main__':
    main()
