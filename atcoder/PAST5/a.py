def main():
    s = input()

    for l in range(5-2):
        for r in range(1, 3):
            if s[l] != s[l+r]:
                break
        else:
            print(s[l])
            return

    print('draw')


if __name__ == '__main__':
    main()
