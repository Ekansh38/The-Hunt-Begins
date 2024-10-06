from pathlib import Path
from time import sleep

from colorama import Fore, Style, init

from load_game import load
from main_loop import main_loop
from player import Player
from utils import clear_screen, is_single_word

init(autoreset=True)

saves_folder = Path(
    "/Users/Ekansh/Desktop/Programming-Projects/The-Hunt-Begins/saves/"
)  # Replace with the path to your folder
files = [f.name for f in saves_folder.iterdir() if f.is_file()]

if len(files) > 0:
    print(Fore.WHITE + "\n1. Saved Games")
    print(Fore.WHITE + "\n2. New Game")
    choice = input("> ")
    if choice == "1":
        player = load(files, saves_folder)
        main_loop(player)


# Charector Creation


ABILITY_POINTS = 25
MAX_POINTS_PER_ABILITY = 10

# clear_screen()

print(Fore.LIGHTYELLOW_EX + "\nWelcome to: " + Fore.RED + "The Hunt Begins!")

input(Fore.LIGHTBLACK_EX + "\nPress Enter to continue...")

clear_screen()

print(Fore.WHITE + "\nIt is time to create your character.\n")


print("What is your name?")
player_name = input("> ")

MAX_NAME_LENGTH = 16

while True:
    if len(player_name) == 0:
        print("\nYou must enter a name.")
        player_name = input("> ")
        continue

    if not is_single_word(player_name):
        print("\nEnter your nickname, not your full name.")
        player_name = input("> ")
        continue
    if len(player_name) > MAX_NAME_LENGTH:
        print(f"\nYour name must be {MAX_NAME_LENGTH} characters or less.")
        player_name = input("> ")
        continue
    if (
        len(player_name) > 0
        and is_single_word(player_name)
        and len(player_name) <= MAX_NAME_LENGTH
    ):
        break

clear_screen()

print("\nWelcome, " + Style.BRIGHT + f"{player_name}!\n")
print("Now, let's assign your ability points.\n")
print(
    "You have "
    + Style.BRIGHT
    + str(ABILITY_POINTS)
    + Style.NORMAL
    + " points to spend on your abilities.\n"
)
print("You can spend them on the following abilities:\n")
print("1. " + Fore.RED + "Strength" + Fore.WHITE + ": Increases your physical damage.")
print(
    "2. "
    + Fore.GREEN
    + "Agility"
    + Fore.WHITE
    + ": Increases your chance to dodge attacks."
)
print(
    "3. " + Fore.BLUE + "Intelligence" + Fore.WHITE + ": Increases your magical damage."
)
print(
    "4. "
    + Fore.YELLOW
    + "Stealth"
    + Fore.WHITE
    + ": Increases your chance to avoid combat.\n"
)

strength = 0
agility = 0
intelligence = 0
stealth = 0

print(
    "Type the number of the ability you want to increase,\nfollowed by the number of points you want to spend, seperated by a colon."
)

print(
    f"The maximum number of points you can spend on an ability is {MAX_POINTS_PER_ABILITY}.\n"
)

while ABILITY_POINTS > 0:
    print(f"\nYou have {ABILITY_POINTS} points left to spend.")
    print(
        "Your current stats are: Strength: "
        + Fore.RED
        + str(strength)
        + Fore.WHITE
        + ", Agility: "
        + Fore.GREEN
        + str(agility)
        + Fore.WHITE
        + ", Intelligence: "
        + Fore.BLUE
        + str(intelligence)
        + Fore.WHITE
        + ", Stealth: "
        + Fore.YELLOW
        + str(stealth)
        + Fore.WHITE
    )

    ability = input("> ")

    if ":" not in ability:
        print("\nPlease enter your ability and points separated by a colon.")
        continue

    ability, points = ability.split(":")

    if not points.isdigit():
        print("\nPlease enter a valid number of points.")
        continue

    points = int(points)

    if points > ABILITY_POINTS:
        print("\nYou do not have enough points to spend.")
        continue

    if ability == "1":
        if strength + points > MAX_POINTS_PER_ABILITY:
            print(
                f"\nYou cannot spend more than {MAX_POINTS_PER_ABILITY} points on strength."
            )
            continue
        strength += points
        ABILITY_POINTS -= points
    elif ability == "2":
        if agility + points > MAX_POINTS_PER_ABILITY:
            print(
                f"\nYou cannot spend more than {MAX_POINTS_PER_ABILITY} points on agility."
            )
            continue
        agility += points
        ABILITY_POINTS -= points
    elif ability == "3":
        if intelligence + points > MAX_POINTS_PER_ABILITY:
            print(
                f"\nYou cannot spend more than {MAX_POINTS_PER_ABILITY} points on intelligence."
            )
            continue
        intelligence += points
        ABILITY_POINTS -= points
    elif ability == "4":
        if stealth + points > MAX_POINTS_PER_ABILITY:
            print(
                f"\nYou cannot spend more than {MAX_POINTS_PER_ABILITY} points on stealth."
            )
            continue
        stealth += points
        ABILITY_POINTS -= points
    else:
        print("\nPlease enter a valid ability.")
        continue


player = Player(player_name, strength, agility, intelligence, stealth)
clear_screen()

print("\n" + Fore.WHITE + "Your character has been created.\n")

print("would you like to save your character? (y/n)")

save = input("> ")
if save.lower() == "y":
    print("\nPlease enter a name for your save file.")
    save_name = input("> ")
    with open(saves_folder / f"{save_name}.txt", "w") as file:
        file.write(
            f"{player.name}\n{player.strength}\n{player.agility}\n{player.intelligence}\n{player.stealth}"
        )
    print("\nYour character has been saved.")
