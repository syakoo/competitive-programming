import math


def lmap(func, iter):
    return list(map(func, iter))


def ring_inv(el: int, p: int) -> int:
    """環の逆元

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


def main(n, s, k):
    nk = math.gcd(n, k)
    if nk == 1:
        k_inv = ring_inv(k, n)
        print((n-s)*k_inv % n)
        return

    if (n-s) % nk == 0:
        ns = (n-s) // nk
        n //= nk
        k //= nk
        k_inv = ring_inv(k, n)
        print(ns*k_inv % n)
    else:
        print(-1)


if __name__ == '__main__':
    t = int(input())
    nsks = [lmap(int, input().split()) for _ in range(t)]
    for n, s, k in nsks:
        main(n, s, k)
