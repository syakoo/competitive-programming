from collections import deque


def main():
    h, w = map(int, input().split())
    M = []
    Dict = {}

    for hi in range(h):
        rows = []
        for wi, c in enumerate(list(input())):
            rows.append(c)
            if c == 'S' or c == 'G':
                Dict[c] = (hi, wi)
            if c in list('abcdefghijklmnopqrstuvwxyz'):
                if c not in Dict:
                    Dict[c] = [(hi, wi)]
                else:
                    Dict[c].append((hi, wi))
        M.append(rows)

    S = Dict['S']
    G = Dict['G']
    q = deque([(*S, 0)])

    while len(q) > 0:
        curS = q.popleft()
        if curS[0] == G[0] and curS[1] == G[1]:
            print(curS[2])
            return
        if M[curS[0]][curS[1]] in list('abcdefghijklmnopqrstuvwxyz'):
            tmp = M[curS[0]][curS[1]]
            M[curS[0]][curS[1]] = curS[2]
            q.extend(map(lambda x: (*x, curS[2] + 1), Dict[tmp]))
            Dict[tmp] = []

        else:
            M[curS[0]][curS[1]] = curS[2]

        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nS = (curS[0] + d[0], curS[1] + d[1], curS[2] + 1)

            if not(0 <= nS[0] < h and 0 <= nS[1] < w):
                continue
            if (M[nS[0]][nS[1]] == '#' or type(M[nS[0]][nS[1]]) == int):
                continue
            q.append(nS)

    print(-1)


if __name__ == '__main__':
    main()
