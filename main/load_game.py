import json
from pathlib import Path
from time import sleep

from colorama import Fore, Style, init

from player import Player
from utils import clear_screen

init(autoreset=True)


def load(files, saves_folder):
    print(Fore.WHITE + "\nChoose a save file:\n")
    for i, file in enumerate(files):
        save_name = file.split(".")[0]
        print(f"{i+1}. {save_name}")
    save_file = input("\n> ")
    try:
        save_file = files[int(save_file) - 1]
    except (ValueError, IndexError):
        clear_screen()
        print(Fore.RED + "\nPlease enter a valid choice.")
        sleep(3)
        clear_screen()
        return load(files, saves_folder)
    with open(saves_folder / save_file, "r") as file:
        # Load JSON data
        data = json.load(file)

        player_name = data["name"]
        strength = data["strength"]
        agility = data["agility"]
        intelligence = data["intelligence"]
        stealth = data["stealth"]

        return Player(player_name, strength, agility, intelligence, stealth)
