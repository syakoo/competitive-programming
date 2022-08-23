from collections import deque


def sliding_window_minimum(xs: list, w: int) -> list:
    """長さ w のスライド最小値を求めるアルゴリズム。🐍syakoo O(N)"""
    result = []
    que = deque()

    for i, x in enumerate(xs):
        while que and que[-1][1] >= x:
            que.pop()

        que.append((i, x))
        result.append(que[0][1])

        if que and que[0][0] <= i+1-w:
            que.popleft()

    return result


def sliding_window_maximum(xs: list, w: int) -> list:
    """長さ w のスライド最大値を求めるアルゴリズム。🐍syakoo O(N)"""
    result = []
    que = deque()

    for i, x in enumerate(xs):
        while que and que[-1][1] <= x:
            que.pop()

        que.append((i, x))
        result.append(que[0][1])

        if que and que[0][0] <= i+1-w:
            que.popleft()

    return result


if __name__ == '__main__':
    xs = [1, 2, 3, 4, 5, 6]
    print(sliding_window_minimum(xs, 3))
    # [1, 1, 1, 2, 3, 4]

    xs = [6, 5, 4, 3, 2, 1]
    print(sliding_window_maximum(xs, 4))
    # [6, 6, 6, 6, 5, 4]
