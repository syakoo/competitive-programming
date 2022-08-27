# uncleared

def lmap(func, iter):
    return list(map(func, iter))


def value(cnt: dict) -> int:
    result = 0
    for k, v in cnt.items():
        result += int(k) * 10 ** (v)

    return result


def main():
    k = int(input())
    s = input()
    t = input()

    s_count = {i: 0 for i in range(1, 10)}
    t_count = {i: 0 for i in range(1, 10)}
    all_count = {i: 0 for i in range(1, 10)}
    for si in s[:-1]:
        si = int(si)
        s_count[si] += 1
        all_count[si] += 1
    for ti in t[:-1]:
        ti = int(ti)
        t_count[ti] += 1
        all_count[ti] += 1

    not_win = 0
    t_win = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j and all_count[i] + 2 > k:
                continue
            elif i != j and (all_count[i] + 1 > k or all_count[j] + 1 > k):
                continue

            s_cnt = s_count.copy()
            s_cnt[i] += 1
            t_cnt = t_count.copy()
            t_cnt[j] += 1
            if value(s_cnt) < value(t_cnt):
                if i == j:
                    t_win += (k - all_count[i])*(k - all_count[i] - 1)
                else:
                    t_win += (k - all_count[i])*(k - all_count[j])
            else:
                if i == j:
                    not_win += (k - all_count[i])*(k - all_count[i] - 1)
                else:
                    not_win += (k - all_count[i])*(k - all_count[j])

    print(t_win / (t_win + not_win))


if __name__ == '__main__':
    main()
