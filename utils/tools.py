import os
import time


def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')                        # Clean the screen


def wait(secons):

    time.sleep(secons)


def charging_screen():

    counter = 0.5
    message = '.....'

    for i in range (0,3):
        clean_screen()
        print(f'charging {message}')
        time.sleep(counter)
        counter += 0.33
        message = message * 2


def show_registers(data):
    pass


def show_one_register(data):

    print(("-----"*20)+"\n")

    for key, value in data.items():
        print(f"{key}: {value}")

    print("\n"+('-----'*20)+"\n")