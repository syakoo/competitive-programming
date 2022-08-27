from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0

    q = deque([A[0]])
    for ai in range(1, len(A)):
        ans += q.popleft()
        q.append(A[ai])
        q.append(A[ai])

    print(ans)


if __name__ == '__main__':
    main()
