


with open('input.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def splitstring(value): #https://www.easytweaks.com/divide-string-halves-python/
    string1, string2 = value[:len(value)//2], value[len(value)//2:]
    return [string1, string2]

commonchars = []

for line in lines: 
    compartiment = splitstring(line)

    
    for char in compartiment[0]:
        for char2 in compartiment[1]:
            if char == char2: 
                commonchars.append(char)
                break
        
        if char == char2:
            break

sum = 0 

for letter in commonchars: 
    if letter.isupper():
        result = ord(letter) - 65
        result += 27
        sum += result
        
    else:
        sum += ord(letter) - 96
        

print(sum)