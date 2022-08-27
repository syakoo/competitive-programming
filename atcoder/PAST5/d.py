def main():
    n = int(input())
    Ss = [input() for _ in range(n)]

    Ss.sort(key=lambda s: (int(s), -len(s)))
    print('\n'.join(Ss))


if __name__ == '__main__':
    main()
