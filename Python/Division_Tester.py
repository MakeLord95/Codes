if __name__ == '__main__':

    nums = []

    for i in range(1, 65535):
        if 65534 % i == 0:
            nums.append(i)

        else:
            continue

    with open("numbers.txt", "a") as outfile:
        outfile.write("Numbers:\n")
        for i in nums:
            outfile.write(f"{str(i)}\n")

