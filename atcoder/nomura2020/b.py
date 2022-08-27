import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    t = input()
    t = '$' + t + '$'

    ans = ['$']
    for i in range(1, len(t)-1):
        if t[i] != '?':
            ans.append(t[i])
        else:
            if t[i-1] == 'P' or ans[-1] == 'P':
                ans.append('D')
            elif t[i+1] == '?' or t[i+1] == 'D':
                ans.append('P')
            else:
                ans.append('D')

    print(''.join(ans[1:]))


if __name__ == '__main__':
    main()
