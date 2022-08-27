

def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w, k = map(int, input().split())
    C = [input() for _ in range(h)]
    ans = 0

    for hbi in range(1, 2**h):
        for wbi in range(1, 2**w):
            bs = 0
            for hi in range(h):
                if not hbi & (1 << hi):
                    continue
                for wi in range(w):
                    if not wbi & (1 << wi):
                        continue
                    if C[hi][wi] == "#":
                        bs += 1
            if bs == k:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
