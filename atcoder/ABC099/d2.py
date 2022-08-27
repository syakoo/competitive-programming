import numpy as np
import itertools

N, C = map(int, input().split())
D = np.array([[int(x) for x in input().split()] for _ in range(C)])
c = np.array([[int(x) for x in input().split()] for _ in range(N)])
c -= 1
cls = np.zeros_like(c)

for i, j in itertools.product([0, 1, 2], [0, 1, 2]):
    cls[i::3, j::3] = (i+j) % 3

# 色の分布 cls, color -> count
color_dist = np.zeros((3, C), dtype=np.int64)
for i in range(3):
    for j in range(C):
        color_dist[i, j] = ((cls == i) & (c == j)).sum()

min_cost = np.inf

for a, b, c in itertools.product(range(C), repeat=3):
    if a == b or a == c or b == c:
        continue
    cost = 0
    cost += (color_dist[0] * D[:, a]).sum()
    cost += (color_dist[1] * D[:, b]).sum()
    cost += (color_dist[2] * D[:, c]).sum()
    min_cost = min(cost, min_cost)

print(min_cost)
