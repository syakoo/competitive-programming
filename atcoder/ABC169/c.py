
def main():
    a, b = input().split()

    print(int(a) * int(b.replace(".", "")) // 100)


if __name__ == '__main__':
    main()
