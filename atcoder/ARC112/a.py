
def lmap(func, iter):
    return list(map(func, iter))


def main():
    t = int(input())
    LRs = [lmap(int, input().split()) for _ in range(t)]

    for l, r in LRs:
        ans = 0
        if r - 2 * l + 1 > 0:
            ans = r - 2 * l + 1
            ans = (ans)*(ans+1) // 2
        print(ans)


if __name__ == '__main__':
    main()
