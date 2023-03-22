import sys

if __name__ == '__main__':
    i = 0

    while i <= 65_534:
        print(i)
        if i < 65_534:
            i += 1057
        else:
            print("Max")
            break

    while i >= 0:
        print(i)
        if i > 0:
            i -= 1057
        else:
            print("Min")
            break
