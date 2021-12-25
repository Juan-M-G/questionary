from models.player import Player
from models.question import Question
from models.level import Level
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
        if op == 3:
            res = input("\nWrite the correct answer and then press Enter.\n")
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


def load_questions():
    questions = []
    try:
        with open(DATA, "r", encoding="utf-8") as f:
            data = f.read()
            jsondata = json.loads(data)
        for line in jsondata:
            question_obj = Question(line["statement"], line["op1"], line["op2"],
                                    line["op3"], line["op4"], line["answer"], line["difficulty"])
            question_obj.set_name = line["category"]
            questions.append(question_obj)
        f.close()
        return questions
    except:
        print("\n\nData questions not found, please put a data before start game")
        input("\nPress Enter to continue....")


def game():
    questions = load_questions()
    lvls = []
    score = 0
    cat_num = len(set(i.get_name for i in questions))

    for i in range(0, cat_num):
        lvls.append(Level(i+1, (i+1)*500))
    for j in lvls:
        clear()
        res = None
        question_group = [
            x for x in questions if j.get_level_number == x.get_difficulty]
        selected_question = question_group[random.randint(
            0, len(question_group) - 1)]
        options = [selected_question.get_op1, selected_question.get_op2,
                   selected_question.get_op3, selected_question.get_op4]
        random.shuffle(options, random.random)
        while res == None:
            print(f"QUESTION {j.get_level_number}".center(50, "="), end=" ")
            print(f"score: {score} \n")
            print(selected_question.get_statement)
            print(f"a) {options[0]}")
            print(f"b) {options[1]}")
            print(f"c) {options[2]}")
            print(f"d) {options[3]}")
            res = validate(3)
        if options[res] == selected_question.get_answer:
            print("¡¡¡¡RESPUESTA CORRECTA!!!!!")
            score += j.get_points
        else:
            print("RESPUESTA INCORRECTA")
        input("\n\nPres Enter to show next question.")



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
            game()
            # Comienza un nuevo juego
        if option == 2:
            show_scores()
        if option == 3:
            clear()
            return "Thanks for playing"


if __name__ == '__main__':
    run()
