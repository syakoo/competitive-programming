# 3 min
n = int(input())
As = list(map(int, input().split()))

cnt = 0
now = 1
for a in As:
    if a == now:
        now += 1
    else:
        cnt += 1

if cnt == n:
    cnt = -1
print(cnt)
