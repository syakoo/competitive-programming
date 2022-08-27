def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    chokudai = 'chokudai'
    cnts = [0]*(len(chokudai) + 1)
    cnts[0] = 1
    MOD = 10**9 + 7

    for i, c in enumerate(s):
        if c in chokudai:
            i = chokudai.index(c)
            cnts[i+1] += cnts[i]
            cnts[i+1] %= MOD

    print(cnts[-1])


if __name__ == '__main__':
    main()
