# 12min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    s = input()
    fox_num = 0
    que = []

    for i in range(n):
        if len(que) != 0:
            if que[-1] == 1 and s[i] == 'o':
                que[-1] = 2
            elif que[-1] == 2 and s[i] == 'x':
                fox_num += 1
                que.pop()
            elif s[i] != 'f':
                que = []

        if s[i] == 'f':
            que.append(1)

    print(n - fox_num * 3)


if __name__ == '__main__':
    main()
