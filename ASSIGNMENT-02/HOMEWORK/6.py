import random

def playRockPaperScissor(rounds):
    player_score = 0
    computer_score = 0
    choices = ["rock", "paper", "scissor"]

    for round in range(1, rounds + 1):
        print(f"Round {round}:")

        player_choice = input("Your choice (rock/paper/scissor): ").lower()
        if player_choice not in choices:
            print("Invalid input. Please choose rock, paper, or scissor.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (
            (player_choice == "rock" and computer_choice == "scissor") or
            (player_choice == "scissor" and computer_choice == "paper") or
            (player_choice == "paper" and computer_choice == "rock")
        ):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

    print(f"Your Score: {player_score}")
    print(f"Computer's Score: {computer_score}")

    if player_score > computer_score:
        print("You have won the game!")
    elif player_score < computer_score:
        print("Computer has won the game!")
    else:
        print("It's a tie!")

# Example usage:
rounds = int(input("Enter the number of rounds: "))
playRockPaperScissor(rounds)
