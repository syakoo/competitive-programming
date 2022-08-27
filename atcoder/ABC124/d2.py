n, k = map(int, input().split())
s = input()

idxs = []
chr = '#'
for i, si in enumerate(s):
    if chr != si:
        idxs.append(i)
        chr = si
idxs.append(n)

ans = 0
for l in range(len(idxs)-1):
    if s[idxs[l]] == '0':
        r = l + 2*k
    else:
        r = l + 2*k + 1

    r = min(r, len(idxs)-1)
    ans = max(ans, idxs[r]-idxs[l])

if ans == 0:
    ans = n

print(ans)
