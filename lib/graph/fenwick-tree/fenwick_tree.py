# a.k.a. BIT (Binary Indexed Tree)
class FenwickTree:
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


A = [1, 2, 3, 4, 5, 6, 7, 8]
FW = FenwickTree(len(A))

for i, a in enumerate(A):
    FW.add(i, a)

print(FW.sum(0, 8))  # 36 (= 1 + 2 + ... + 8)
print(FW.sum(1, 8))  # 35 (= 2 + 3 + ... + 8)
print(FW.sum(4, 6))  # 11 (= 5 + 6)
