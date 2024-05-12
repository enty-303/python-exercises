def check_gues(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('The answer is correct.')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('The answer is incorrect. Try again.')
            attempt = attempt + 1
    if attempt == 3:
        print('right answer: ' + answer)
score = 0
print('"Test "Adeptus Astartres"')
guess1 = input('What weapons do tactical guards have?')
check_gues(guess1, 'bolter and combat blade')
guess2 = input('In which company are the terminators?')
check_gues(guess2, 'in the first company')
guess3 = input('Who produces the space marine armor?')
check_gues(guess3, 'Adeptus Mechanicus')
print('You scored points: ' + str(score))