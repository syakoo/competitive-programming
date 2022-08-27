
def main():
    n = int(input())
    S = [input() for _ in range(n)]
    setS = set()

    for s in S:
        if s[0] == "!" and s[1:] in setS:
            print(s[1:])
            return
        elif f'!{s}' in setS:
            print(s)
            return

        setS.add(s)

    print("satisfiable")


if __name__ == '__main__':
    main()
