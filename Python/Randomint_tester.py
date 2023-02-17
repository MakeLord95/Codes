import random

def count_array(arr, nbr):
    return arr.count(nbr)

array = []

for _ in range(250000):
    num = random.randint(1, 10)
    array.append(num)

for x in range(1, 10):
    print(f"{x}", end=": ")
    y = count_array(array, x)
    p = y / 250000 * 100
    print(f"{p:.2f}%")
