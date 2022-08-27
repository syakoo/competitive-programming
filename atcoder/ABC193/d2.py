
def lmap(func, iter):
    return list(map(func, iter))


def score(cards: list):
    res = 0
    for i in range(1, 10):
        res += i*(10**(cards.count(i)))

    return res


def main():
    k = int(input())
    s = lmap(int, input()[:-1])
    t = lmap(int, input()[:-1])
    cnt = [k] * 10
    cnt[0] = 0

    for si, ti in zip(s, t):
        cnt[si] -= 1
        cnt[ti] -= 1

    t_win = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if cnt[i] < 1 or cnt[j] < 1 or (i == j and cnt[i] < 2):
                continue

            if score(s+[i]) > score(t+[j]):
                t_win += (cnt[i])*(cnt[i] - 1) if i == j else cnt[i] * cnt[j]

    all_mt = sum(cnt) * (sum(cnt) - 1)
    print(t_win / all_mt)


if __name__ == '__main__':
    main()
