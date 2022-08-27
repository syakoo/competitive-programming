
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, q = map(int, input().split())
    Qs = [input().split() for _ in range(q)]
    Fss = [['N' for _ in range(n)] for _ in range(n)]
    def id(x): return int(x) - 1

    for q in Qs:
        if q[0] == '1':
            Fss[id(q[1])][id(q[2])] = 'Y'
        elif q[0] == '2':
            for i in range(n):
                if Fss[i][id(q[1])] == 'Y':
                    Fss[id(q[1])][i] = 'Y'
        else:
            idxes = []
            for i in range(n):
                if Fss[id(q[1])][i] == 'Y':
                    for j in range(n):
                        if id(q[1]) != j and Fss[i][j] == 'Y':
                            idxes.append(j)

            for idx in idxes:
                Fss[id(q[1])][idx] = 'Y'

    print('\n'.join(''.join(fs) for fs in Fss))


if __name__ == '__main__':
    main()
