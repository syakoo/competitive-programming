
def main():
    s = input()
    t = input()
    ans = 1000

    for i in range(len(s)-len(t)+1):
        m = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                m += 1

        ans = min(ans, m)

    print(ans)


if __name__ == '__main__':
    main()
