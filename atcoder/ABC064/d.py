# 5 min
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    s = input()

    l_cnt = 0
    cnt = 0
    for si in s:
        if si == '(':
            cnt += 1
        else:
            if cnt == 0:
                l_cnt += 1
            else:
                cnt -= 1

    print('('*l_cnt + s + ')' * cnt)


if __name__ == '__main__':
    main()
