# 11 min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    counts = [0] * (10**5 + 1)

    for a in As:
        counts[a] += 1

    ans = 0
    even_counts = 0
    for c in counts:
        if c == 0:
            continue
        if c % 2 == 1:
            ans += 1
        else:
            ans += 1
            even_counts += 1

    print(ans if even_counts % 2 == 0 else ans - 1)


if __name__ == '__main__':
    main()
