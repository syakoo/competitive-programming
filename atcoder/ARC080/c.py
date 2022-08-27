def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    cnts = [0]*3

    for a in As:
        if a % 4 == 0:
            cnts[2] += 1
        elif a % 2 == 0:
            cnts[1] += 1
        else:
            cnts[0] += 1

    oddcnt = cnts[0]
    if cnts[1]:
        oddcnt += 1
    if oddcnt > cnts[2]+1:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    main()
