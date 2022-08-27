
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    As = lmap(int, input().split())
    S = {}
    for i in range(m):
        if As[i] in S:
            S[As[i]] += 1
        else:
            S[As[i]] = 1

    for i in range(0, n-m):
        if As[i + m] in S:
            S[As[i + m]] += 1
        if As[i] in S:
            S[As[i]] -= 1
            if S[As[i]] == 0:
                del S[As[i]]

    for i in range(n + 2):
        if i not in S:
            print(i)
            return


if __name__ == '__main__':
    main()
