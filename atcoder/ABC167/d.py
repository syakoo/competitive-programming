def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    As = [0] + lmap(int, input().split())
    A_map = dict()
    cur_city = 1

    while True:
        if k == 0:
            print(cur_city)
            return

        if cur_city in A_map and (A_map[cur_city] - k) < k:
            k %= (A_map[cur_city] - k)
        else:
            A_map[cur_city] = k
            k -= 1
            cur_city = As[cur_city]


if __name__ == '__main__':
    main()
