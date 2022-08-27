# 17 min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    Bs = [0]*n
    ans = []

    for i in range(n-1, -1, -1):
        cnt = 0
        for j in range(i, n, i+1):
            cnt += Bs[j]
            cnt %= 2

        if cnt != As[i]:
            Bs[i] = 1
            ans.append(i + 1)
    
    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    main()
