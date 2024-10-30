from clear_console import clear

def choice():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    chosen_word_done = False
    
    while not chosen_word_done:
        valid = True
        chosen_word = input('''
    Please choose the word that the person will guess:
    (Must be beetween 2 and 30 characters)

    > ''')
        for letter in chosen_word.lower():
            if not letter in alphabet:
                valid = False
                break
              
        if not (len(chosen_word) < 2 or len(chosen_word) > 30) and valid:
            chosen_word_done = True
        else:
            clear()
            print('Please Type a word that has 2-30 characters and that has no symbols in it.')

    return chosen_word