with open('input.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def splitstring(value): #https://www.easytweaks.com/divide-string-halves-python/
    string1, string2 = value[:len(value)//2], value[len(value)//2:]
    return [string1, string2]

tab = []
commonchars = []
for i in range(2, len(lines), 3):
     for char in lines[i]:
        for char2 in lines[i - 1]:
            if char == char2: 
                for char3 in lines[i - 2]: 
                    if char2 == char3: 
                        commonchars.append(char3)
                        break
                if char2 == char3:
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