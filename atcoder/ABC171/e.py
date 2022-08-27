
def main():
    n = int(input())
    A = list(map(int, input().split()))
    if n == 2:
        print(A[1], A[0])
        return

    ans = [0]
    for ai in range(1, n):
        xor_as = A[ai-1] ^ A[ai]
        ans.append(xor_as ^ ans[ai-1])
    
    bias = A[0]
    for a in ans[1:]:
        bias ^= a

    print(' '.join(str(a ^ bias) for a in ans))


if __name__ == '__main__':
    main()
