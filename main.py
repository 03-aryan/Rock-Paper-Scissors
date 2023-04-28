import random


def get_choices():
    player_choice = input("Input your choice rock, paper or scissors: ")
    options = ["rock", "paper", "scissor"]
    print(options)
    computer_choice = random.choice(options)
    choices = {"Player": player_choice, "Computer": computer_choice}
    return choices



def check_win(player, computer):

 print(f"You chose {player}, Computer chose {computer}")
 if computer == player:
         return "it's a tie"
 elif player == "rock":
     if computer == "scissors":
         return "rock smashes paper! you win!"
     else:
         return "paper covers rock! you lose"
 elif player =="paper":
    if computer =="scissors":
         return "scissor cuts paper! you lose."
    else:
         return "paper covers rock! WIN!"
 elif player == "scissors":
    if computer == "rock":
         return "rock smashes scissor! you lose."
    else:
         return "scissor cuts paper! win!"

choices = get_choices()
result = check_win(choices["Player"],choices["Computer"])
print(result) 
