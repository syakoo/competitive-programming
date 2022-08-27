
def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    dig = '1234567890'
    if s[0] in dig and s[1] in dig and s[2] in dig:
        print(int(s) * 2)
        return

    print('error')


if __name__ == '__main__':
    main()
