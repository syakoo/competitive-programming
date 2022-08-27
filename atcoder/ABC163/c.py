
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    ans = [0] * n
    for a in As:
        ans[a - 1] += 1

    print('\n'.join(str(a) for a in ans))


if __name__ == '__main__':
    main()
