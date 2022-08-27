from collections import Counter

n = int(input())
As = list(map(int, input().split()))

cnt = 0
for k, v in Counter(As).items():
    if v >= k:
        cnt += v - k
    else:
        cnt += v

print(cnt)
