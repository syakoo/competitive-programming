
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s1 = input()
    s2 = input()
    s3 = input()

    ss = set(s for s in s1 + s2 + s3)
    dic = {s: -1 for s in ss}

    s1_e = s1[-1]
    s2_e = s2[-1]
    s3_e = s3[-1]
    if s1_e == s2_e == s3_e:
        dic[s1_e] = 0
        
    elif s1_e == s3_e:
        dic[s2_e] = 0
        pass
    elif s2_e == s3_e:
        dic[s1_e] = 0
        pass
    elif s1_e == s2_e:
        pass
    else:
        pass


if __name__ == '__main__':
    main()
