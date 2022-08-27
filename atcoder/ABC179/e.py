# uncleared

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
    n, x, m = map(int, input().split())
    fw = FenwickTree(m)
    fw.add(0, x)
    dic = {x: 0}
    j = 0

    for i in range(1, m + 1):
        j = i
        x = (x ** 2) % m
        if x in dic:
            break
        dic[x] = i
        fw.add(i, x)

    if n <= j:
        print(fw.sum(0, n))
    else:
        print(fw.sum(0, j) + fw.sum(dic[x], j + 1)*((n-j) //
                                                    (j-dic[x])) + fw.sum(dic[x], dic[x]+(n-j) % (j-dic[x])))


if __name__ == '__main__':
    main()
