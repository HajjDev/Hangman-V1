def convert(word):
    output = ''
    
    for _ in range(len(word)):
        if _ != len(word) - 1:
            output += '_ '
        else:
            output += '_'
        
    return output