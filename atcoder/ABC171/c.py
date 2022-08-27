
def main():
    """26進数"""
    n = int(input())

    names = []
    x = n
    while x:
        x -= 1
        x, r = divmod(x, 26)
        names.append(chr(ord('a') + r))

    print(''.join(reversed(names)))


if __name__ == '__main__':
    main()
