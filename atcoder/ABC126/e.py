# 3 min

class UnionFind():
    def __init__(self, n: int):
        """Union Findð

        Args:
            n (int): å¨ä½ã®åæ°
        """
        self.n = n
        self.parents = [-1] * n

    def find(self, x: int):
        """xçªç®ã®è¦ç´ ã®è¦ªãæã£ã¦ãã. < O(log N)"""
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x: int, y: int):
        """ x ã¨ y ããã£ã¤ãã"""
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x: int):
        return -self.parents[self.find(x)]

    def same(self, x: int, y: int):
        """ x ã¨ y ãåãã°ã«ã¼ããã©ãã"""
        return self.find(x) == self.find(y)

    def members(self, x: int):
        """ x ã¨åãã°ã«ã¼ãã®ãã¤ãæã£ã¦ãã"""
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """æ ¹ã¨ãªã£ã¦ããã¤ãæã£ã¦ãã"""
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """ã°ã«ã¼ãã®æ°"""
        return len(self.roots())

    def all_group_members(self):
        """å¨ã°ã«ã¼ãã®ã¡ã³ãã¼ãæã£ã¦ãã"""
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    XYZs = [lmap(int, input().split()) for _ in range(m)]

    uf = UnionFind(n)
    for x, y, _ in XYZs:
        uf.union(x-1, y-1)

    print(uf.group_count())


if __name__ == '__main__':
    main()
