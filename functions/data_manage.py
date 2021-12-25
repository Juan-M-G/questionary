from functions.auxiliar import clear, os, validate
from models.player import Player
from models.question import Question
from DIR.constant import *
import json

# Class that load the questions for the game from a json file, and return a list of objects question type
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
        input(CONTINUE_TXT)

# Save the player's score to a json file. Max 5 scores and order from highest to lowest
def save_score(score):
    name = "                       "
    while len(name) > 10:
        name = input("\n\nPut your name (max 10 characters): ")
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
    clear()

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
        input(CONTINUE_TXT)

def clear_scores():
    clear()
    while True:
        res = validate(2,1)
        if res == "Y" or res == "N":
            break
    if res == "Y": 
        if os.path.exists(LEADERBOARD):
            os.remove(LEADERBOARD)
        else:
            print("\n\nLeaderboards not fount, please play a game first")
            input(CONTINUE_TXT)
    else:
        return