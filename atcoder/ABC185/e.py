
def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    lenA = len(A)
    lenB = len(B)
    dif_len = abs(lenA - lenB)

    dp = [[0 for _ in range(dif_len + 1)] for _ in range(min(lenA, lenB) + 1)]
    for n in range(1, lenA, lenB + 1):
        for k in range(1, dif_len + 1):
            pass


if __name__ == '__main__':
    main()
