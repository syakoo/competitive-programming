from collections import deque


def set_tree(maps, st: int, n: int) -> list:
    result = [-1 for _ in range(n + 1)]
    q = deque([(-1, st)])

    while len(q) > 0:
        par, you = q.popleft()
        for nex in maps[you]:
            if par == nex:
                continue
            q.append((you, nex))
            result[nex] = you

    return result


def seek_ans(Cs: list, maps: dict, st: int) -> list:
    q = deque([(-1, st)])

    while len(q) > 0:
        par, you = q.popleft()
        for nex in maps[you]:
            if par == nex:
                continue

            q.append((you, nex))
            Cs[nex] += Cs[you]

    return Cs


def main():
    n = int(input())
    ABs = [list(map(int, input().split())) for _ in range(n - 1)]
    q_num = int(input())
    Qs = [list(map(int, input().split())) for _ in range(q_num)]
    maps = {}
    for a, b in ABs:
        if a in maps:
            maps[a].append(b)
        else:
            maps[a] = [b]
        if b in maps:
            maps[b].append(a)
        else:
            maps[b] = [a]

    Cs = [0 for _ in range(n + 1)]
    nodes = set_tree(maps, 1, n)

    for t, e, x in Qs:
        a, b = ABs[e - 1]
        if t == 1:
            if nodes[a] == b:
                Cs[a] += x
            else:
                Cs[1] += x
                Cs[b] -= x
        else:
            if nodes[b] == a:
                Cs[b] += x
            else:
                Cs[1] += x
                Cs[a] -= x

    Cs = seek_ans(Cs, maps, 1)
    print('\n'.join(str(c) for c in Cs[1:]))


if __name__ == '__main__':
    main()
