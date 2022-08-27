
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = input()
    m_di = len(n)
    dis = [0] * m_di

    if m_di < 3:
        print(0)
        return

    dis[0] = int(n) - int('9' * (m_di - 1))
    for i in range(m_di - 1, 0, -1):
        dis[m_di - i] = (10 ** (i - 1)) * 9

    ans = 0
    for i, d in enumerate(dis[::-1]):
        ans += d*(i // 3)

    print(ans)


if __name__ == '__main__':
    main()
