
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    A = lmap(int, input().split())
    B = lmap(int, input().split())

    ans = 0
    for ai, bi in zip(A, B):
        ans += ai * bi

    print(['No', 'Yes'][int(ans == 0)])


if __name__ == '__main__':
    main()
