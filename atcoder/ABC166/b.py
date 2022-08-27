
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    cnts = [0] * n

    for _ in range(k):
        _ = input()
        for a in map(int, input().split()):
            cnts[a - 1] += 1

    ans = cnts.count(0)
    print(ans)


if __name__ == '__main__':
    main()
