from models.player import Player
from DIR.constant import *
import random

import os
import json

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def validate(op):
    try:
        if op == 1:
            res = int(input("Choose an option: "))
            if res > 4 or res < 1:
                raise
        if op == 2:
            res = input("Do you want to continue?: Y/N: ")
            if res.upper() != "Y" and res.upper() != "N":
                print(res.upper() != "N")
                raise
        return res
    except:
        input("Select a valid option.")

def load_questions():
    try:
        with open(DATA, "r", encoding = "utf-8") as f:
            data = f.read()
            jsondata = json.loads(data)
        for line in range(len(jsondata)):
            txt = f"{line + 1}. " + jsondata[line]["name"]
            print(txt.ljust(20, "."), end=" ")
            print(jsondata[line]["score"])
        input("\n\nPress Enter to continue....")
        f.close()
    except:
        print("\n\nLeaderboards not fount, please play a game first")
        input("\nPress Enter to continue....")

def show_scores():
    pass

def run():
    option = 0
    while option != 4:
        clear()
        print("WElCOME TO QUESTIONARY GAME".center(50, "="))
        print("\n\n1. New Game.\n")
        print("2. Leaderboards.\n")
        print("3. Exit.\n")
        option = validate(1)
        if option == 1:
            pass
            #Comienza un nuevo juego
        if option == 2:
            show_scores()
        if option == 3:
            clear()
            return "Thanks for playing"

if __name__ == '__main__':
    run()