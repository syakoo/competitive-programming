# 20min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    cnt = dict()
    lst_s = ''
    ans = 0

    for i, si in enumerate(s[::-1]):
        if lst_s == si:
            ans += i - cnt[si]
            cnt = {si: i + 1}
        else:
            if si in cnt:
                cnt[si] += 1
            else:
                cnt[si] = 1
        lst_s = si

    print(ans)


if __name__ == '__main__':
    main()
