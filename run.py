import random
import colorama
from random import randint
from os import system, name

colorama.init()

# Initialize the game boards
def init_boards(size):
    return [['.' for _ in range(size)] for _ in range(size)]




if __name__ == "__main__":
    while True:
        print("     \033[1m**ULTIMATE NAVAL WAR**\033    ")
        input("\nPress any KEY to enter the game...")

