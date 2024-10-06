from utils import clear_screen


def main_loop(player):
    clear_screen()
    print("Welcome to the main loop!\nYour character is:")
    print(player.name)
    print("Strength:", player.strength)
    print("Agility:", player.agility)
    print("Intelligence:", player.intelligence)
    print("Stealth:", player.stealth)
