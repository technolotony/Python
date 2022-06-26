import os
import requests as r

def get_random_word():
    # Get a random word from this random word API 
    uri = 'https://random-word-api.herokuapp.com/word'
    word = (r.get(uri)).json()[0]
    return word

def render_hangman(wrongGuessCount): 
    # Create the hangman based on how many guesses the player got wrong 
    match wrongGuessCount:
        case 0: person = print('''
        ------------
        |
        |
        |
        |
        _____
        ''')
        case 1: person = print( '''
        ------------
        |          O
        |
        |
        |
        _____
        ''')
        case 2: person = print( '''
        ------------
        |          O
        |          | 
        |
        |
        _____
        ''')
        case 3: person = print( '''
        ------------
        |          O
        |          | 
        |          |
        |         
        _____
        ''')
        case 4: person = print( '''
        ------------
        |          O
        |          | 
        |          |
        |         /
        _____
        ''')
        case 5: person = print( '''
        ------------
        |          O
        |          | 
        |          |
        |         / \\
        _____
        ''')
        case 6: person = print( '''
        ------------
        |          O
        |          | -
        |          |
        |         / \\
        _____
        ''')
        case 7: person = print( '''
        ------------
        |          O
        |        - | -
        |          |
        |         / \\
        _____
        ''')
    return person

def render_lowerbars(word):
    # Dynamically create the lower bars and return the bars array 
    bars = []
    for i in word: 
        bars.append("_")
    return bars

def main(): 
    # ANSI colors/commands used by our print statements 
    reset = '\u001b[0m'
    colors = {
        "incorrect": '\u001b[31m',
        "correct": '\u001b[32m',
        "error": '\u001b[33m'

    }
    # Get the random word 
    word = get_random_word()

    hasWon = False 
    wrongGuessCount = 0 
    MaxGuessCount = 7
    lettersCorrect = []
    lettersWrong = []
    lowerbars = render_lowerbars(word)

    while hasWon == False: 
        print( "Correct Guesses =", lettersCorrect ) 
        print( "Inorrect Guesses =", lettersWrong ) 
        render_hangman(wrongGuessCount)
        print(lowerbars)
        lowerbarsAsString = "".join(lowerbars)

        # If our word = our lower bars, the player has won and should not guess again. 
        if word == lowerbarsAsString: 
                    print(colors["correct"],"You won!",reset) 
                    hasWon = True
                    break
        
        # Receive user input for a guess 
        guess = input('Pick a letter: ').lower()
        
        # Make sure the guess is only 1 character 
        if len(guess) == 1: 
            if guess in lettersCorrect or guess in lettersCorrect: 
                print(colors['error'],"Letter already guessed. Please guess again", reset)
                continue
            # If the guess was correct: 
            if guess in word:
                # Initalize our Index_pos variable
                # This is the index of the bars list that the character was last found in 
                index_pos = 0
                print(colors['correct'],"Correct Guess!",reset)
                lettersCorrect.append(guess)
                complete = False
                while complete == False:
                    try: 
                        letterindex = word.index(guess, index_pos)
                        index_pos = letterindex + 1
                        lowerbars[letterindex] = guess
                    # Once we've searched the whole string for our guess an exception will be thrown. 
                    # Catch that exception and assign the complete variable. 
                    except: 
                        complete = True

            else: 
                # If we haven't hit our max guess count yet, let the user continue trying. 
                if wrongGuessCount < MaxGuessCount:
                    wrongGuessCount += 1
                    print(colors["incorrect"],"Guess Incorrect. Try again!",reset)
                    # Add the wrong guess to our lettersWrong list 
                    lettersWrong.append(guess)
                    continue
                else: 
                    # If we have hit our max guess count, end the game. 
                    print(colors['error'],"Game lost :(",reset)
                    break

        else:
            # Throw an error if a user provided the same guess multiple times. 
            print(colors['error'],"Input invalid. Please provide only one letter.",reset)
            continue
    print("Game Over! The word was: " + word)
main() 
