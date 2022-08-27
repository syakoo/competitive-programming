
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    A = lmap(int, input().split())

    a_max = max(A[:2**(n-1)])
    b_max = max(A[2**(n-1):])
    semi = min(a_max, b_max)

    for i, ai in enumerate(A):
        if semi == ai:
            print(i + 1)


if __name__ == '__main__':
    main()
