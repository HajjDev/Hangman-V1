from clear_console import clear
from convert_word import convert
from chosen_word import choice
from user_ui import user
from after_game import after

stopped = False

def main():
    game_finished = False
    game_started = False
    sure = False
    chances_chosen = False
    loaded = False

    while not game_started:
        game_start = input('''
Hello and welcome to the best hangman game in python!
    
Well, not exaclty a hangman game but a similar one and even funnier!
Play with your friends and enjoy.

Type `yes` to start: ''')
        
        if game_start.lower() == 'yes':
            game_started = True
        else:
            clear()
            print("You can only start the game here, you can't type something else.")

    clear()

    chosen_word = choice()
    converted_word = convert(chosen_word)
    clear()

    while not sure:
        print(f'''
You chose this word: {chosen_word}

That will translate to: {convert(chosen_word)}
''')
        decision = input('''
Do you want to keep it?
Type `yes` or `no`

> ''')
        
        if decision.lower() == 'yes':
            clear()
            break
        elif decision.lower() == 'no':
            clear()
            chosen_word = choice()
            clear()
        else:
            clear()
            print('Please type an accepted command.')

    while not chances_chosen:
        try:
            chances = int(input('''
How many chances would you give your opponent to guess your word ?

> '''))
            
            if chances > 0:
                chances_chosen = True
                clear()
            else:
                clear()
                print('Please choose a number that is higher than 0.')
            
        except ValueError:
            clear()
            print('Please choose a number!')

    while not game_finished:
        
        while not loaded:
            started = input(f'''
Hey! It is your turn now to guess the word chosen by your opponent!

for this round, you have:
Lives : {chances}
So you can guess a wrong letter only {chances} time/s !

GoodLuck !

Type `start` to start the game.
> ''')
            if started == 'start':
                loaded = True
                clear()
            else:
                clear()
                print('Please type `start` to continue.')

        user(chances, convert(chosen_word), chosen_word)
        game_finished = True

while not stopped:
    main()
    if not after():
        stopped = True