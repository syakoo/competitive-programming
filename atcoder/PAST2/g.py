from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    q = int(input())
    Qs = [input().split() for _ in range(q)]

    que = deque()
    curr_query = ('', 0)
    for q in Qs:
        if q[0] == '1':
            que.append((q[1], int(q[2])))
            continue

        dels = dict()
        d = int(q[1])
        if curr_query[1] != 0:
            if curr_query[1] >= d:
                val = d
                curr_query = (curr_query[0], curr_query[1] - d)
                d = 0
            else:
                val = curr_query[1]
                d -= curr_query[1]
                curr_query = (curr_query[0], 0)

            if curr_query[0] in dels:
                dels[curr_query[0]] += val
            else:
                dels[curr_query[0]] = val

        while que and d > 0:
            item = que.popleft()
            if item[1] > d:
                val = d
                curr_query = (item[0], item[1] - d)
                d = 0
            else:
                val = item[1]
                d -= item[1]

            if item[0] in dels:
                dels[item[0]] += val
            else:
                dels[item[0]] = val

        ans = 0
        for val in dels.values():
            ans += val**2

        print(ans)


if __name__ == '__main__':
    main()
