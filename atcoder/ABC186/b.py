# 3min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    Ass = [lmap(int, input().split()) for _ in range(h)]
    s = 0
    m = 100

    for As in Ass:
        for a in As:
            m = min(m, a)
            s += a

    print(s - m*h*w)


if __name__ == '__main__':
    main()
