import os

def clear():
    '''
    pre : void
    post : Clears the console from any text>
    
    This function is used to clear the console.
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    