from itertools import permutations


def lmap(func, iter):
    return list(map(func, iter))


def main():
    As = lmap(int, input().split())

    for a1, a2, a3 in permutations(As):
        if a3 - a2 == a2 - a1:
            print('Yes')
            return

    print('No')


if __name__ == '__main__':
    main()
