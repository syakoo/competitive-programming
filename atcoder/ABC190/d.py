
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    cnt = 1

    for i in range(2, n):
        sp = n / i
        if sp - i//2 <= 0:
            break

        if i % 2 == 0 and (sp * 10) % 10 == 5:
            cnt += 1
        elif i % 2 == 1 and (sp * 10) % 10 == 0:
            cnt += 1

    print(cnt * 2)


if __name__ == '__main__':
    main()
