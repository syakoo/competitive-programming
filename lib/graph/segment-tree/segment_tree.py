class SegmentTree:
    def __init__(self, size: int, f=lambda x, y: x+y, e=0):
        """1-indexed の非再帰型セグメント木

        Args:
            size (int): 配列のサイズ
            f ((x, y) -> z): モノイドの演算。デフォルトは和
            e (Any): モノイドの単位元。デフォルトは 0
        """
        self.size = 2 ** (size - 1).bit_length()
        self.e = e
        self.nodes = [e] * (self.size*2)
        self.f = f

    def get(self, i: int):
        """ i 番目の要素を取得する

        Args:
            i (int): i-th
        """
        return self.nodes[i + self.size]

    def update(self, i: int, x):
        """ i 番目を x にする

        Args:
            i (int): i-th
            x (Any): モノイドの元
        """
        i += self.size
        self.nodes[i] = x
        while i > 0:
            i >>= 1
            self.nodes[i] = self.f(self.nodes[i*2], self.nodes[i*2 + 1])

    def query(self, l: int, r: int):
        """[l, r) の区間に対して演算をする. O(log n)

        Args:
            l (int): 左
            r (int): 右

        Returns:
            Any: モノイドの元
        """
        l += self.size
        r += self.size
        lres, rres = self.e, self.e

        while l < r:
            if l & 1:
                lres = self.f(lres, self.nodes[l])
                l += 1

            if r & 1:
                r -= 1
                rres = self.f(self.nodes[r], rres)

            l >>= 1
            r >>= 1

        res = self.f(lres, rres)
        return res


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    # 加法におけるセグメント木
    sg = SegmentTree(len(arr))

    for i, a in enumerate(arr):
        sg.update(i, a)

    print(sg.nodes)  # [120, 36, 10, 26, 3, 7, 11, 15, 1, 2, 3, 4, 5, 6, 7, 8]
    print(sg.get(3))  # 4
    print(sg.query(0, 8))  # 36 = 1 + 2 + ... + 8
    print(sg.query(0, 4))  # 10 = 1 + 2 + ... + 4

    # max におけるセグメント木
    sg2 = SegmentTree(len(arr), max)

    for i, a in enumerate(arr):
        sg2.update(i, a)

    print(sg2.nodes)  # [8, 8, 4, 8, 2, 4, 6, 8, 1, 2, 3, 4, 5, 6, 7, 8]
    print(sg2.get(3))  # 4
    print(sg2.query(0, 8))  # 8 = max(1, 2, ..., 8)
    print(sg2.query(0, 4))  # 4 = max(1, 2, ..., 4)
