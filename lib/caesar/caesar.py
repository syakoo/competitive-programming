def str_rshift(s: str, i: int):
    result = []
    for c in s:
        code = (ord(c) - ord('a') + i) % 26
        result.append(chr(code + ord('a')))

    return ''.join(result)


if __name__ == '__main__':
    s = 'helloworld'
    ct = str_rshift(s, 7)
    print(ct)
    me = str_rshift(ct, -7)
    print(me)
