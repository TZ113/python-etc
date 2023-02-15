import random
import sys

CODE_LENGTH = 4
MAX_TRIES = 10
COLORS = ['R', 'G', 'B', 'Y', 'V', 'O', 'I']

def generate_code(colors):
    code = []
    [code.append(random.choice(colors)) for i in range(4)]
    return code


def take_guess(tr, colors):
    while True:
        res = input(f'Please enter your colors separated by space, you have {MAX_TRIES - tr} tries left. [example:- R G B Y] ')
        guess = res.upper().split()
        if len(guess) != CODE_LENGTH:
            print('We must have four colors!')
            return
        elif any([color.upper() not in colors for color in guess]):
            print('Valid colors are:- ', *colors)
            return
        break
    
    return guess
    

#this is what coding is really about.. dumbhead.. 
def check(original_code, guess_code):
    correct_pos = 0
    incorrect_pos = 0
    
    """    
    original_code, guess_code = original_code.copy(), guess_code.copy()
    correct_pos_indices = []
    for idx, colors in enumerate(zip(guess_code, original_code)):
        if colors[0] == colors[1]:
            correct_pos += 1
            correct_pos_indices.append(idx)
    for i in correct_pos_indices:
        original_code.pop(i)
        guess_code.pop(i)

    for color in guess_code:
        if color in original_code:
            incorrect_pos += 1
            original_code.remove(color)
            
            --this is messy--
    """           

    counter = {}
    for color in original_code:
        if color in counter:
            counter[color] += 1
        else:
            counter[color] = 0
    
    for original, guess in zip(original_code, guess_code):
        if original == guess:
            correct_pos += 1
            counter[guess] -= 1
    
    for guess in guess_code:
        if guess in counter and counter[guess] > 0:
            incorrect_pos += 1
            counter[guess] -= 1
            
    return correct_pos, incorrect_pos


def game():
    while True:
        intro = input('Welcome to mastermind! In this game you must guess my code if you want to win! Do you want to continue? [press enter..] ')
        if intro == '':
            break
    code = generate_code(COLORS)
    print(id(code))   
    for i in range(MAX_TRIES):
        guess = take_guess(i, COLORS)
        if guess:
            correct_pos, incorrect_pos = check(code, guess)
            if correct_pos == CODE_LENGTH:
                sys.exit(f"You've guessed my code in {i + 1} tries!")
            else:
                print(f"Correct positions:- {correct_pos} | incorrect positions:- {incorrect_pos}")
        
    print('You have no more tires!')
        
        
if __name__ == "__main__":
    game()