import random as rd

n = 10
print(n)
print(*[rd.randint(1, 10**3) for _ in range(n)])
