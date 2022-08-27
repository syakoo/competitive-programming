
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, C = map(int, input().split())
    ABCs = [lmap(int, input().split()) for _ in range(n)]
    days = {}

    for a, b, c in ABCs:
        if a in days:
            days[a] += c
        else:
            days[a] = c
        if b + 1 in days:
            days[b + 1] -= c
        else:
            days[b + 1] = -c

    ans = 0
    day_keys = list(days.keys())
    day_keys.sort()
    for dki in range(1, len(day_keys)):
        days[day_keys[dki]] += days[day_keys[dki - 1]]
        ans += min(days[day_keys[dki - 1]], C) * (day_keys[dki] - day_keys[dki - 1])

    print(ans)


if __name__ == '__main__':
    main()
