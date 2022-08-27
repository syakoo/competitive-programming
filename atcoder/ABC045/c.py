from itertools import product


def main():
    s = input()
    ans = 0

    for sps in product([0, 1], repeat=len(s)-1):
        tmp = int(s[0])
        for i in range(len(s)-1):
            if sps[i]:
                ans += tmp
                tmp = int(s[i+1])
            else:
                tmp *= 10
                tmp += int(s[i+1])
        ans += tmp

    print(ans)


if __name__ == '__main__':
    main()
