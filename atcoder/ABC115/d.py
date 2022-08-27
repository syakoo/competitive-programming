
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, x = map(int, input().split())
    Ls = [0] * n
    Ps = [0] * n
    Ls[0] = 5
    Ps[0] = 3
    for i in range(1, n):
        Ls[i] = 2*Ls[i - 1] + 3
        Ps[i] = 2*Ps[i - 1] + 1

    def solve(l, d) -> int:
        if d <= 1:
            return 0

        if l == 0:
            return min(3, d - 1)

        if d <= Ls[l-1] + 1:
            return solve(l - 1, d - 1)
        elif d == Ls[l - 1] + 2:
            return Ps[l - 1] + 1

        return Ps[l - 1] + 1 + solve(l - 1, d - Ls[l - 1] - 2)

    print(solve(n - 1, x))


if __name__ == '__main__':
    main()
