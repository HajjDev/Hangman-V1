from clear_console import clear

def after():
    answered = False
    
    while not answered:
        answer = input('''
Do you wish to start a new game?
- Yes
- No

> ''').lower()
        
        if answer == 'yes':
            clear()
            return True
        elif answer == 'no':
            clear()
            print('Thank you for playing.')
            return False
        else:
            clear()
            print('Please type `yes`or `no`.')