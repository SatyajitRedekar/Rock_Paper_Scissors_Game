import random
import asset

compu = ["rock", "paper", "scissors"]
name = str(input("what is your name : "))
while True :

    computer_choice = random.choice(compu)
    human_choice = str(input("what is your choice (Rock , Paper , Scissors) : ").lower())

    if human_choice == "t" :
        break

    # for the human choice
    if (human_choice == "rock" or human_choice == "r") or human_choice == "r" :
        print(asset.rock)
    elif (human_choice == "paper" or human_choice == "p") or human_choice == "p" :
        print(asset.paper)
    elif (human_choice == "scissors" or human_choice == "r") or human_choice == "s" :
        print(asset.scissors)
    elif human_choice != compu :
        print("enter the valid choice !")
        break

    # computer choice
    print(f"computer choice : {computer_choice}")
    if computer_choice == "rock" :
        print(asset.rock)
    elif computer_choice == "paper" :
        print(asset.paper)
    elif computer_choice == "scissors" :
        print(asset.scissors)


    if human_choice == computer_choice :
        print("this is draw !")
    elif (human_choice == "rock" or human_choice == "r") and computer_choice == "paper" :
        print("You lose !")
    elif (human_choice == "paper" or human_choice == "p" )and computer_choice == "scissors" :
        print("You lose !")
    elif (human_choice == "scissors" or human_choice == "s") and computer_choice == "rock":
        print("You lose !")
    else:
        print(f"{name} is won !")
    print("if you want to stop this game press t")
