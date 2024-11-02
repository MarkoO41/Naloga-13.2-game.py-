
import datetime
import random
import json

# dodamo class in ga definiramo
class result:
    def __init__(self, attempts, player_name, date):
        self.attempts = attempts
        self.player_name = player_name
        self.date = date

def play_game(level):
    secret = random.randint(1, 30)
    attempts = 0
    score_list = get_score_list()
    player_name = input(f"Enter your name: ")

    while True:
        guess = int(input("Guess the number between 1 and 30: "))
        attempts += 1

        if guess == secret:
            result_obj = result(attempts=attempts, player_name=player_name, date=str(datetime.datetime.now()))  # rezultate priredimo, kot slovar        
           
            print(f"Congrats! {attempts} needed.")
            current_time = datetime.datetime.now()
            score_list.append(result_obj.__dict__)             # spremenimo da listo v jsonu prikazuje kot slovar
            
            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))
            break
        elif guess > secret and level=="easy":
            print("Try something lower.")
        elif guess < secret and level=="easy":
            print("Try something higher.")
        else:
            print("Your guess is not correct!")

def get_score_list():
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list
    
def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda k: k["attempts"])[:3]
    return top_score_list

    
while True:
    select = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

    if select.upper() == "A":
        level = input("Choose your level (easy/hard): ")
        play_game(level)
    elif select.upper() == "B":
        for score_dict in get_top_scores():            # dodamo, da prikaz shrajenih podatkov v jsonu prikazuje kot slovar
            result_obj = result(attempts=score_dict.get("attempts"),
                                player_name=score_dict.get("player_name", "Anonymous"),
                                date=score_dict.get("date"))

            print("Player: {name}; Attempts: {attempts}; Date: {date}".format(name=result_obj.player_name,
                                                                              attempts=result_obj.attempts,
                                                                              date=result_obj.date))
            
    else:
        break