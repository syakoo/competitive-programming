
def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    Ss = []

    l = -1
    for i in range(len(s)):
        if s[i].isupper():
            if l == -1:
                l = i
            else:
                Ss.append(s[l:i+1])
                l = -1
    Ss.sort(key=lambda x: x.lower())

    print(''.join(Ss))


if __name__ == '__main__':
    main()
