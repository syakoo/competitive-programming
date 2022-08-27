
# 52 min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    b, c = map(int, input().split())
    pos_c = c if b > 0 else c - 1
    neg_c = c - 1 if b > 0 else c
    if c == 1:
        print(2 if b != 0 else 1)
        return
    if b < 0:
        b = -b

    pos_range = [b - pos_c // 2, 0]
    neg_range = [-b - neg_c // 2, 0]
    pos_range[1] = -neg_range[0] if neg_c % 2 == 1 else -neg_range[0]-1
    neg_range[1] = -pos_range[0] if pos_c % 2 == 1 else -pos_range[0]-1

    ans = pos_range[1] - max(0, pos_range[0]) + \
        min(-1, neg_range[1]) - neg_range[0] + 2

    print(ans)


if __name__ == '__main__':
    main()
