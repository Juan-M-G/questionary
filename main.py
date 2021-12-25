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
            res = res.upper()
            if res != "Y" and res != "N":
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
    next_q = None

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
            print(f"QUESTION {j.get_level_number}==CATEGORY: {selected_question.get_name}".center(
                50, "="), end=" ")
            print(f"score: {score} \n")
            print(selected_question.get_statement)
            print(f"a) {options[0]}")
            print(f"b) {options[1]}")
            print(f"c) {options[2]}")
            print(f"d) {options[3]}")
            res = validate(3)
        if options[res] == selected_question.get_answer:
            # print("\n¡¡¡¡RESPUESTA CORRECTA!!!!!")
            score += j.get_points
        else:
            print("RESPUESTA INCORRECTA")
            return save_score([0, j.get_level_number])
        if j.get_level_number == len(lvls):
            clear()
            print(f"YOU WIN, CONGRATULATIONS".center(50, "="), end=" ")
            return save_score([score, j.get_level_number])
        while next_q == None:
            next_q = validate(2)
        if next_q == "Y":
            next_q = None
        else:
            return save_score([score, j.get_level_number])


def save_score(score):
    clear()
    name = "                       "
    while len(name) > 10:
        name = input("Put your name (max 10 characters): ")
    try:
        with open(LEADERBOARD, "r", encoding="utf-8") as f:
            data = f.read()
            jsondata = json.loads(data)
    except:
        jsondata = []
        pass
    user = Player(name, score[1], score[0])
    with open(LEADERBOARD, "w", encoding="utf-8") as f:
        jsondata.append({
            "name": user.get_name,
            "round": user.get_level,
            "score": user.get_score
        })
        for i in range(len(jsondata)):
            for j in range(len(jsondata)):
                if int(jsondata[i]["score"]) > int(jsondata[j]["score"]):
                    aux = jsondata[j]
                    jsondata[j] = jsondata[i]
                    jsondata[i] = aux
        if len(jsondata) > 5:
            jsondata.pop(len(jsondata)-1)
        json.dump(jsondata, f, indent=4)
    f.close()


def show_scores():
    clear()
    try:
        with open(LEADERBOARD, "r", encoding="utf-8") as f:
            data = f.read()
            jsondata = json.loads(data)
        print("*********************************".center(50, "="))
        print("LEADERBOARDS".center(50, "="))
        print("*********************************".center(50, "=")+"\n")
        for line in range(len(jsondata)):
            txt = f"{line + 1}. " + jsondata[line]["name"]
            print(txt.ljust(20, "."), end=" ")
            print(
                f"Level: {jsondata[line]['round']}..Score: {jsondata[line]['score']}")
        input("\n\nPress Enter to continue....")
        f.close()
    except:
        print("\n\nLeaderboards not fount, please play a game first")
        input("\nPress Enter to continue....")


def clear_scores():
    clear()
    if os.path.exists("./save/leaderboards.json"):
        os.remove("./save/leaderboards.json")
    else:
        print("\n\nLeaderboards not fount, please play a game first")
        input("\nPress Enter to continue....")

def run():
    while True:
        clear()
        print("WElCOME TO QUESTIONARY GAME".center(50, "="))
        print("\n\n1. New Game.\n")
        print("2. Leaderboards.\n")
        print("3. Clean leaderboards.\n")
        print("4. Exit.\n")
        option = validate(1)
        if option == 1:
            game()
        if option == 2:
            show_scores()
        if option == 3:
            clear_scores()
        if option == 4:
            clear()
            return "Thanks for playing"

if __name__ == '__main__':
    run()
