import math


def main():
    N, m, T = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(m)]
    n = N
    t = 0

    for a, b in AB:
        at = (a - t)
        if at > 0.5:
            n -= 1 + int(at - 0.5)
        t = a
        if n <= 0:
            print("No")
            return

        ba = b - a
        if ba > 0.5:
            n = min(n + 1 + int(ba - 0.5), N)
        t = b

    Tt = (T - t)
    if Tt > 0.5:
        n -= 1 + int(Tt - 0.5)
    if n <= 0:
        print("No")
        return

    print("Yes")


if __name__ == '__main__':
    main()
