# 6 min

def main():
    s = input()

    sets = set(['A', 'C', 'G', 'T'])
    mx = 0
    for w in range(1, len(s)+1):
        for l in range(len(s) - w + 1):
            flg = True
            for i in range(l, l+w):
                if s[i] not in sets:
                    flg = False
                    break

            if flg:
                mx = w

    print(mx)


if __name__ == '__main__':
    main()
