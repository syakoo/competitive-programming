from itertools import permutations


def main():
    n, k = map(int, input().split())
    Tss = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for vs in permutations(range(1, n)):
        dist = Tss[0][vs[0]] + Tss[0][vs[-1]]
        for vi in range(n - 2):
            dist += Tss[vs[vi]][vs[vi + 1]]

        if dist == k:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
