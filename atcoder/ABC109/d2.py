def main():
    h, w = map(int, input().split())
    Ass = [list(map(int, input().split())) for _ in range(h)]

    cmds = []
    for hi in range(h):
        dw = 1 if hi % 2 == 0 else -1
        wi = 0 if hi % 2 == 0 else w-1

        while 0 <= wi + dw < w:
            if Ass[hi][wi] % 2:
                Ass[hi][wi+dw] += 1
                cmds.append(f'{hi+1} {wi+1} {hi+1} {wi+1+dw}')

            wi += dw

        if Ass[hi][wi] % 2 and hi+1 < h:
            Ass[hi+1][wi] += 1
            cmds.append(f'{hi+1} {wi+1} {hi+2} {wi+1}')

    print(len(cmds))
    print('\n'.join(cmds))


if __name__ == '__main__':
    main()
