
def lmap(func, iter):
    return list(map(func, iter))


def find_start_p(h, w, Sss):
    for hi in range(h):
        for wi in range(w):
            if Sss[hi][wi] == '#':
                return (hi, wi - 1)


def main():
    h, w = map(int, input().split())
    Sss = [input() for _ in range(h)]
    ans = 0
    start_pos = find_start_p(h, w, Sss)
    pos = start_pos
    directs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dire_num = 0

    while pos != start_pos or dire_num != 0 or not ans:
        next_dire_num = (dire_num + 1) % 4
        next_pos = (pos[0] + directs[next_dire_num][0],
                    pos[1] + directs[next_dire_num][1])
        if Sss[next_pos[0]][next_pos[1]] == '.':
            ans += 1
            dire_num = next_dire_num
            pos = next_pos
            continue

        next_pos = (pos[0] + directs[dire_num][0],
                    pos[1] + directs[dire_num][1])
        if Sss[next_pos[0]][next_pos[1]] == '#':
            ans += 1
            dire_num = (dire_num - 1) % 4
            continue

        pos = next_pos

    print(ans)


if __name__ == '__main__':
    main()
