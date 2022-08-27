
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    As = lmap(int, input().split())
    ans = max(-1, n - sum(As))
    print(ans)


if __name__ == '__main__':
    main()
