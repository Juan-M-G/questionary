from functions.auxiliar import *
from functions.data_manage import *
from models.level import Level
import random

# In this function there is the logic of the game 
def game():
    # Receive all questions data
    questions = load_questions()
    lvls = []
    score = 0
    # Calculate the number of categories avaliables
    cat_num = len(set(i.get_name for i in questions))
    # Create levels/rounds according to the number of categories
    for i in range(0, cat_num):
        lvls.append(Level(i+1, (i+1)*500))
    # In this for, is selected the question for the level, according with the difficulty
    for j in lvls:
        clear()
        res = None
        # Create a list of only questions with a difficulty level equal to the current level
        question_group = [
            x for x in questions if j.get_level_number == x.get_difficulty]
        # Select one question ramdom
        selected_question = question_group[random.randint(
            0, len(question_group) - 1)]
        # Keeps all options of the question in a List, and then shuffle it
        options = [selected_question.get_op1, selected_question.get_op2,
                   selected_question.get_op3, selected_question.get_op4]
        random.shuffle(options, random.random)
        # Print the selected question
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
        # Validate the answer
        if options[res] == selected_question.get_answer:
            score += j.get_points
        else:
            clear()
            print("INCORRECT ANSWER......YOU LOSE EVERYTHING")
            return save_score([0, j.get_level_number])
        # Validate if the player finish the game
        if j.get_level_number == len(lvls):
            clear()
            print(f"YOU WIN, CONGRATULATIONS".center(50, "="), end=" ")
            return save_score([score, j.get_level_number])
        # Ask to the player if he want to continue playing
        while True:
            next_q = validate(2)
            if next_q == "Y" or next_q == "N":
                break
        if next_q == "N":
            clear()
            return save_score([score, j.get_level_number])

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
