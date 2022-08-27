# 2h 14min

def lmap(func, iter):
    return list(map(func, iter))


class FenwickTree:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: int):
        """FW_p に x を足す

        Args:
            p (int): インデックス
            x (int): 値
        """
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, l: int, r: int) -> int:
        """l ~ r の和を求める

        Args:
            l (int): 左のインデックス
            r (int): 右のインデックス

        Returns:
            int: 和
        """
        return self._sum(r) - self._sum(l)

    def _sum(self, r: int) -> int:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s


def main():
    n = int(input())
    As = lmap(int, input().split())
    fw = FenwickTree(n)
    t = 0

    for i, a in enumerate(As):
        t += fw.sum(a, n)
        fw.add(a, 1)

    for i in range(n):
        print(t)
        t += n - 1 - (As[i]*2)


if __name__ == '__main__':
    main()
