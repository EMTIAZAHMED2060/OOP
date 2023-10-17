import random
def playRockPaperScissor(rounds) :
    human_score = 0
    machine_score = 0
    for i in range(rounds) :
        hum = input('Your turn: ')
        mec = random.choice(['Rock','Paper','Scissor'])
        print('Computer:',mec)

        if hum == 'Rock' and mec == 'Paper' :
            machine_score += 1
        elif mec == 'Rock' and hum == 'Paper' :
            human_score += 1
        elif hum == 'Rock' and mec == 'Scissor' :
            human_score += 1
        elif hum == 'Scissor' and mec == 'Rock' :
            machine_score += 1


        elif hum == 'Paper' and mec == 'Scissor' :
            machine_score += 1
        elif hum == 'Scissor' and mec == 'Paper' :
            human_score += 1

        elif hum == mec :
            human_score += 0
            machine_score += 0
    print(f'Your score: {human_score}')
    print(f"Computer's score: {machine_score}")

    if machine_score > human_score :
        print('Computer has won the game!')
    elif machine_score < human_score :
        print('You have won the game!')
    else :
        print('Tied!')

playRockPaperScissor(3)