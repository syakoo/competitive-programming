
def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    Ass = [lmap(int, input().split()) for _ in range(h)]
    odd_cells = []

    for hi in range(h):
        for wi in range(w):
            if Ass[hi][wi] % 2 == 1:
                odd_cells.append((hi, wi))

    movements = []
    for i in range(0, len(odd_cells) - 1, 2):
        _from = odd_cells[i]
        _to = odd_cells[i+1]
        movements.extend([(hj+1, _from[1]+1, hj+2, _from[1]+1)
                          for hj in range(_from[0], _to[0])])

        if _from[1] > _to[1]:
            movements.extend([(_to[0]+1, wj+1, _to[0]+1, wj)
                              for wj in range(_from[1], _to[1], -1)])
        else:
            movements.extend([(_to[0]+1, wj + 1, _to[0] + 1, wj + 2)
                              for wj in range(_from[1], _to[1])])

    print(len(movements))
    print('\n'.join(' '.join(lmap(str, move)) for move in movements))


if __name__ == '__main__':
    main()
