from time import sleep

from colorama import Fore, Style, init

from player import Player
from utils import clear_screen, is_single_word

init(autoreset=True)


# Charector Creation


ability_points = 25

clear_screen()

print(Fore.LIGHTYELLOW_EX + "Welcome to: " + Fore.RED + "The Hunt Begins!")

input(Fore.LIGHTBLACK_EX + "\nPress Enter to continue...")

clear_screen()

print(Fore.WHITE + "\nIt is time to create your character.\n")


print("What is your name?")
player_name = input("> ")

while True:
    if len(player_name) == 0:
        print("\nYou must enter a name.")
        player_name = input("> ")
        continue

    if not is_single_word(player_name):
        print("\nEnter your nickname, not your full name.")
        player_name = input("> ")
        continue
    if len(player_name) > 10:
        print("\nYour name must be 10 characters or less.")
        player_name = input("> ")
        continue
    if len(player_name) > 0 and is_single_word(player_name) and len(player_name) <= 10:
        break

clear_screen()

print("\nWelcome, " + Style.BRIGHT + f"{player_name}!\n")
print("Now, let's assign your ability points.\n")
print("You have 25 points to spend on your abilities.\n")
print("You can spend them on the following abilities:\n")
print("Strength: Increases your physical damage.")
print("Agility: Increases your chance to dodge attacks.")
print("Intelligence: Increases your magical damage.")
print("Stealth: Increases your chance to avoid combat.\n")
