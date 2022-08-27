
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    As = [int(input()) for _ in range(n)]
    count = 0
    ans = 0

    for i in range(k-1):
        if As[i + 1] - As[i] > 0:
            count += 1

    if count == k - 1:
        ans += 1

    for i in range(n - k):
        if As[i+1] - As[i] > 0:
            count -= 1
        if As[i+k] - As[i+k-1] > 0:
            count += 1

        if count == k - 1:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
