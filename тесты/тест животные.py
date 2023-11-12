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
print('"Test "animals"')
guess1 = input('What kind of bear lives in the arctic circle?')
check_gues(guess1, 'polar bear')
guess2 = input('Which land animal is the fastest?')
check_gues(guess2, 'cheetah')
guess3 = input('Which animal is the biggest?')
check_gues(guess3, 'the blue whale')
print('You scored points: ' + str(score))