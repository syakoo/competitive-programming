
def field_inv(el: int, p: int) -> int:
    """体の逆元

    Args:
        el (int): 体の元
        p (int): 素数
    """
    return pow(el, p-2, p)


def ring_inv(el: int, p: int) -> int:
    """環の逆元. O(log el)

    Args:
        el (int): 環の元
        p (int): 法
    """
    # el*a + p*b = 1 の a を求める
    m = p
    a, la = 0, 1
    while p != 0:
        q = el // p
        el, p = p, el % p
        a, la = la - q*a, a

    return la % m


if __name__ == '__main__':
    p = 7
    print(field_inv(2, p))
    print(field_inv(3, p))
    print(field_inv(4, p))

    p = 8
    print(ring_inv(3, p))
    print(ring_inv(5, p))
