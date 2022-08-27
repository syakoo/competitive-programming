
def lmap(func, iter):
    return list(map(func, iter))


def main():
    x, k, d = map(int, input().split())

    if abs(x) >= d*k:
        print(abs(x) - d*k)
        return

    rest_times = abs(x) // d - k
    if rest_times % 2 == 0:
        print(abs(x) % d)
    else:
        print(d - (abs(x) % d))


if __name__ == '__main__':
    main()
