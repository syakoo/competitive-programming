
def lmap(func, iter):
    return list(map(func, iter))


def solve(d: int, Ss) -> int:
    if d == 0:
        return 1

    if Ss[d - 1] == 'AND':
        return solve(d - 1, Ss)
    else:
        return solve(d - 1, Ss) + 2**d


def main():
    n = int(input())
    Ss = [input() for _ in range(n)]
    print(solve(n, Ss))


if __name__ == '__main__':
    main()
