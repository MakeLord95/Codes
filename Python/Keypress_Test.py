import time
import random
from pynput.keyboard import Controller

if __name__ == '__main__':
    keyboard = Controller()

    time.sleep(2)
    print('Start')

    key_dict = {
        0: 'w',
        1: 'a',
        2: 's',
        3: 'd'
    }

    while True:
        key_to_press = key_dict[random.randint(0, 3)]
        keyboard.press(key_to_press)

        hold_time = random.uniform(0.1, 0.5)
        print(f'Holding \'{key_to_press}\' for {hold_time}s')
        time.sleep(hold_time)

        keyboard.release(key_to_press)

        wait_time = random.uniform(32, 64)
        print(f'Sleeping for {wait_time}s')
        time.sleep(wait_time)
