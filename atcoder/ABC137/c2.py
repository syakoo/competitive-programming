from collections import Counter


def main():
    n = int(input())

    Ss = [''.join(sorted(input())) for _ in range(n)]
    cnts = Counter(Ss)

    ans = sum(v*(v-1)//2 for _, v in cnts.items())
    print(ans)


main()
