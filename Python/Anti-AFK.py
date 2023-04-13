from time import sleep
from random import uniform, randint
from pynput.keyboard import Controller


def respawn_pets(kb):
    print('Respawning pets')

    kb.press('r')

    key_hold_time = uniform(0.001, 0.005)
    sleep(key_hold_time)

    kb.release('r')

    return


def sleep_period(sec):
    print(f"Sleeping for {sec // 60}m and {sec % 60}s")

    while sec > 0:
        sec -= 1
        print(f"Remaining: {sec // 60}m and {sec % 60}s")
        sleep(1)


if __name__ == '__main__':
    keyboard = Controller()

    sleep_period(5)
    print('Start')

    while True:
        respawn_pets(keyboard)

        wait_time = randint(450, 525)
        sleep_period(wait_time)

        respawn_pets(keyboard)
        sleep(0.5)

        wait_time = randint(450, 525)
        sleep_period(wait_time)
