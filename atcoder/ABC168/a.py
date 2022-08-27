
def main():
    n = int(input()) % 10
    hon = [2, 4, 5, 7, 9]
    pon = [0, 1, 6, 8]
    bon = [3]

    if n in hon:
        print("hon")
    elif n in pon:
        print("pon")
    elif n in bon:
        print("bon")


if __name__ == '__main__':
    main()
