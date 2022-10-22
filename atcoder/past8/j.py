import math
import sys

sys.setrecursionlimit(10**9)


class FenWickTree:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: int):
        """FW_p に x を足す. O(log N)

        Args:
            p (int): インデックス
            x (int): 値
        """
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, l: int, r: int) -> int:
        """l ~ r の和を求める. O(log N)

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


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, q = map(int, input().split())
    TKs = [lmap(int, input().split()) for _ in range(q)]

    fw = FenWickTree(n)

    for t, k in TKs:
        if t == 1:
            if k > n:
                x = fw.sum(0, 2*n - k + 1) % 2
            else:
                x = fw.sum(0, k) % 2

            print(k if x == 0 else 2*n - k + 1)
        else:
            x = fw.sum(n - k, n - k+1)
            if x == 0:
                fw.add(n-k, 1)
            else:
                fw.add(n-k, -1)


if __name__ == '__main__':
    main()
