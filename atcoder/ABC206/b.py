def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())

    cnt = 0
    for i in range(10**8):
        cnt += i
        if cnt >= n:
            print(i)
            return


if __name__ == '__main__':
    main()
