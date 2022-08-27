# 36 min
from collections import Counter


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()

    if len(s) <= 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print("Yes")
        else:
            print("No")
        return

    s_cnt = Counter(s)
    for i in range(112, 1000, 8):
        if not Counter(str(i)) - s_cnt:
            print("Yes")
            return

    print("No")


if __name__ == '__main__':
    main()
