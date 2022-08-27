
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    ABCD = lmap(int, list(input()))

    for ops in range(1 << 3):
        ans = ABCD[0]
        for opi in range(3):
            if ops & (1 << opi):
                ans += ABCD[opi + 1]
            else:
                ans -= ABCD[opi + 1]

        if ans == 7:
            eq = str(ABCD[0])
            for opi in range(3):
                if ops & (1 << opi):
                    eq += '+' + str(ABCD[opi + 1])
                else:
                    eq += '-' + str(ABCD[opi + 1])

            print(eq + '=7')
            return


if __name__ == '__main__':
    main()
