def main():
    n = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    Adict = dict()
    sum_A = sum(A)
    # O(n)
    for a in A:
        if a in Adict:
            Adict[a] += 1
        else:
            Adict[a] = 1

    # O(Q)
    for b, c in BC:
        if b in Adict:
            sum_A += (c-b)*Adict[b]
            if c in Adict:
                Adict[c] += Adict[b]
            else:
                Adict[c] = Adict[b]
            Adict[b] = 0

        print(sum_A)


if __name__ == '__main__':
    main()
