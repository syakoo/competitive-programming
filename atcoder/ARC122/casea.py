import itertools as it

n = int(input())
As = list(map(int, input().split()))

ans = 0
for subAs in it.product(*map(lambda x: (x, -x), As)):
    for ai, aj in zip(subAs, subAs[1:]):
        if ai < 0 and aj < 0:
            break
    else:
        if subAs[0] > 0:
            ans += sum(subAs)

print(ans)
