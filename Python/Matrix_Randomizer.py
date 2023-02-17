import numpy
import random


def create_matrix():
    rows = 3
    columns = 3
    matrix = []

    for _ in range(rows):
        row = []

        for _ in range(columns):
            value = random.randint(1, 10)
            row.append(value)

        matrix.append(row)

    return matrix


if __name__ == '__main__':

    count = int(input("How many matrises to generate: "))
    for x in range(count):

        matrix_result = create_matrix()
        det = numpy.linalg.det(matrix_result)
        det = round(det, 2)

        for i in matrix_result:
            print(i)

        print(f"Determinant = {det}")

        with open("matrix.txt", "a") as outfile:
            outfile.write(f"Matrix:\n")

            for i in matrix_result:
                outfile.write(str(i))
                outfile.write("\n")

            outfile.write(f"Determinant = {det}\n")
            outfile.write("\n")
