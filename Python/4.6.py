import math
import random
import multiprocessing


def calculate_pi(points):
    circle_points = 0
    square_points = 0

    for i in range(points):
        random_x = random.uniform(-1, 1)
        random_y = random.uniform(-1, 1)

        origin_dist = random_x ** 2 + random_y ** 2

        if origin_dist <= 1:
            circle_points += 1

        square_points += 1

    return 4 * circle_points / square_points


def main():
    user = int(input("Syötä pisteiden määrä: "))
    user_int = int(math.pow(user, 2))
    num_processes = 6  # choose the number of processes

    # create a list of processes
    pool = multiprocessing.Pool(processes=num_processes)

    # calculate the number of points for each process
    points_per_process = user_int // num_processes

    # create a list of arguments for the calculate_pi function
    args_list = [points_per_process] * num_processes

    # calculate the results using multiple processes
    pi_approximations = pool.map(calculate_pi, args_list)

    # calculate the average of the results
    pi = sum(pi_approximations) / len(pi_approximations)

    print(f"Piin likiarvo: {pi}")


if __name__ == "__main__":
    main()
