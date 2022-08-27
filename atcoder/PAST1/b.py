
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = [int(input()) for _ in range(n)]

    for i in range(n - 1):
        sub = As[i + 1] - As[i]
        if sub == 0:
            print('stay')
        elif sub < 0:
            print(f'down {abs(sub)}')
        else:
            print(f'up {abs(sub)}')


if __name__ == '__main__':
    main()
