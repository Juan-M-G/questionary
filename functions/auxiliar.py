import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
# Class that validates all options received by a player
def validate(op, op2=0):
    try:
        if op == 1:
            res = int(input("Choose an option: "))
            if res > 4 or res < 1:
                raise
        if op == 2:
            if op2==0:
                res = input("Correct!! Do you want to continue?: Y/N: ")
            elif op2==1:
                res = input("Are you sure: Y/N: ")
            res = res.upper()
            if res != "Y" and res != "N":
                raise
        if op == 3:
            res = input("\nSelect the correct answer and then press Enter.\n")
            res = res.upper()
            if res != "B" and res != "A" and res != "C" and res != "D":
                raise
            if res == "A":
                res = 0
            if res == "B":
                res = 1
            if res == "C":
                res = 2
            if res == "D":
                res = 3
        return res
    except:
        input("Select a valid option.")
        clear()