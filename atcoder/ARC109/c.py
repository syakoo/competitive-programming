# 27min

def main():
    n, k = map(int, input().split())
    s = input()
    s_l = list(s)
    for _ in range(k):
        if len(s_l) % 2 != 0:
            s_l += s_l
        s_l = solve(s_l)

    print(s_l[0])


def solve(s: list) -> list:
    result = []
    for i in range(0, len(s)-1, 2):
        if s[i] == 'R' and s[i+1] == 'R':
            result.append('R')
        elif s[i] == 'R' and s[i+1] == 'P':
            result.append('P')
        elif s[i] == 'R' and s[i+1] == 'S':
            result.append('R')
        elif s[i] == 'S' and s[i+1] == 'R':
            result.append('R')
        elif s[i] == 'S' and s[i+1] == 'P':
            result.append('S')
        elif s[i] == 'S' and s[i+1] == 'S':
            result.append('S')
        elif s[i] == 'P' and s[i+1] == 'R':
            result.append('P')
        elif s[i] == 'P' and s[i+1] == 'P':
            result.append('P')
        elif s[i] == 'P' and s[i+1] == 'S':
            result.append('S')

    return result


if __name__ == '__main__':
    main()
