# 34 min

def lmap(func, iter):
    return list(map(func, iter))


def bin_search(Xs: list, l: int, r: int):
    def seek(b: int): return sum(map(lambda x: abs(x - b), Xs))
    if r - l <= 2:
        return min(seek(l), seek(r))

    c = (r - l)//2 + l
    if seek(c) < seek(c + 1):
        return bin_search(Xs, l, c)
    else:
        return bin_search(Xs, c + 1, r)


def main():
    n = int(input())
    As = lmap(int, input().split())
    As_b = lmap(lambda x: x[1] - x[0] - 1, enumerate(As))

    print(bin_search(As_b, -10**9, 10**9))


if __name__ == '__main__':
    main()
