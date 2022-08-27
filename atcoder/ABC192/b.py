
def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    for i, si in enumerate(s):
        if i % 2 == 0 and si.isupper():
            print('No')
            return
        elif i % 2 == 1 and si.islower():
            print('No')
            return
    print('Yes')


if __name__ == '__main__':
    main()
