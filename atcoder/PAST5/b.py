def main():
    n = int(input())
    s = input()
    s_set = set()
    ans = []

    for c in s[::-1]:
        if c not in s_set:
            ans.append(c)
            s_set.add(c)

    print(''.join(ans[::-1]))


if __name__ == '__main__':
    main()
