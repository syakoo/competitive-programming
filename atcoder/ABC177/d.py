from collections import deque


# def main():
#     n, m = map(int, input().split())
#     is_checked = [False for _ in range(n+1)]
#     edges = [[] for _ in range(n+1)]
#     ans = 0

#     for _ in range(m):
#         a, b = map(int, input().split())
#         edges[a].append(b)
#         edges[b].append(a)

#     for ni in range(n):
#         if is_checked[ni]:
#             continue
#         is_checked[ni] = True
#         q = deque([ni])
#         depth = 0
#         while len(q) > 0:
#             p = q.popleft()
#             for e in edges[p]:
#                 if not is_checked[e]:
#                     is_checked[e] = True
#                     q.append(e)
#             depth += 1

#         ans = max(ans, depth)

#     print(ans)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    n, m = map(int, input().split())
    uf = UnionFind(n)

    for _ in range(m):
        a, b = map(int, input().split())
        uf.union(a-1, b-1)
    
    sizes = [uf.size(i) for i in range(n)]
    
    print(max(sizes))


if __name__ == '__main__':
    main()
