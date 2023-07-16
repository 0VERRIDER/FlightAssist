import os
import time

def clear_terminal(timed = False):
    if timed:
        time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title = None):
    width = 30
    if not title:
        print("+" * width)
        print("Flight Booking System".center(width))
    else:
        print("+" * width)
        print(title.center(width))
    print("+" * width)

