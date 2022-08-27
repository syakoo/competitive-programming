
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ABs = [lmap(int, input().split()) for _ in range(n)]
    ABs.sort(key=lambda x: x[0] + x[1], reverse=True)
    ans = sum(map(lambda x: x[1][x[0] % 2]*((-1)**(x[0] % 2)), enumerate(ABs)))
    print(ans)


if __name__ == '__main__':
    main()
