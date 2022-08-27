# 8 min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    x = input()
    x_len = len(x)
    s_cnt = 0
    cnt = 0

    for xi in x:
        if xi == 'S':
            s_cnt += 1
        else:
            if s_cnt > 0:
                s_cnt -= 1
                cnt += 1

    print(x_len - 2 * cnt)


if __name__ == '__main__':
    main()
