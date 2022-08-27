# 13 min
def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    k = int(input())

    subs = [set() for _ in range(k)]
    for si in range(len(s)):
        for ki in range(k):
            if si + ki < len(s):
                subs[ki].add(s[si:si+ki+1])

    ssubs = []
    for ki in range(k):
        subs[ki] = sorted(subs[ki])
        for i in range(min(k, len(subs[ki]))):
            ssubs.append(subs[ki][i])

    print(sorted(ssubs)[k-1])


if __name__ == '__main__':
    main()
