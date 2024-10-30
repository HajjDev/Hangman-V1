from clear_console import clear
from convert_word import convert
from letter_chosen import letter

def user(chances, pattern, word):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    done = False
    
    while not done:
        first_pattern = pattern
        letter_chosen = False
        print(f'''

Python - Hangman V1

Lives left : {chances}
Letters : {pattern.count('_')}

Word to guess : {pattern}            
''')
        while not letter_chosen:
            let = input('Please type the letter you want to guess: ')
            if len(let) != 1:
                print('You cannot cheat! Choose 1 letter.')
            elif let.isdigit() or not let in alphabet:
                print("You cannot choose a number or a special character, please choose a letter.")
            else:
                letter_chosen = True
                clear()
        
        pattern = letter(word, let, first_pattern)
        if pattern == first_pattern:
            if chances > 0:
                chances -= 1
                print(f'''
The letter {let} is not part of the word.
You have now {chances} chances left!''')
                
        else:
            print("You found a letter!")

        if chances == 0:
            done = True
            clear()
            print(f'''
You failed to guess the word!

The word chosen by your opponent was: {word}
Good Luck next time!

I hope you enjoyed playing this game. First game made
by me.  
''')
        elif not "_" in pattern:
            done = True
            clear()
            print(f'''
Congratulations!
You won, and guessed the word: {word} with {chances} chances left!

I hope you enjoyed playing this game. First game made
by me.                  
''')
            