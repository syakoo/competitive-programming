from itertools import product


def main():
    s = input()
    # 使用する文字(x 以外)
    digs = []
    # 必須の文字(o)
    requires = set()

    for i, si in enumerate(s):
        if si != 'x':
            digs.append(i)
        if si == 'o':
            requires.add(i)

    cnt = 0
    # 使う数字から 4 桁のパスワードを生成する
    for password in product(digs, repeat=4):
        digset = set(password)
        # 生成したパスワードが必須の文字を包含しているときにカウント
        if digset.issuperset(requires):
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
