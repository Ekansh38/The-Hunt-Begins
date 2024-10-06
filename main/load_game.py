from pathlib import Path
from time import sleep

from colorama import Fore, Style, init

from player import Player
from utils import clear_screen

init(autoreset=True)


def load(files, saves_folder):
    print(Fore.WHITE + "\nChoose a save file:")
    for i, file in enumerate(files):
        save_name = file.split(".")[0]
        print(f"{i+1}. {save_name}")
    save_file = input("> ")
    save_file = files[int(save_file) - 1]
    with open(saves_folder / save_file, "r") as file:
        data = file.read().splitlines()
        player_name = data[0]
        strength = int(data[1])
        agility = int(data[2])
        intelligence = int(data[3])
        stealth = int(data[4])
        return Player(player_name, strength, agility, intelligence, stealth)
