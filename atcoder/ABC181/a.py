# 1 min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    print(['White', 'Black'][n % 2])


if __name__ == '__main__':
    main()
