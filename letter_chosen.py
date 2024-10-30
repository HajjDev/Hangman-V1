def letter(word, letter, pattern):
    list = pattern.split(' ')
    output = ''
    worded = []
    
    for el in word.lower():
        worded.append(el)
        
    for let in worded:
        if let == letter:
            list[worded.index(let)] = letter
            worded[worded.index(let)] = '-'
    
    for index in range(len(list)):
        if index != len(list) - 1:
            output += list[index] + ' '
        else:
            output += list[index]
            
    return output