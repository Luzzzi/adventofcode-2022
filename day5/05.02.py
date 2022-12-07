import re 

with open('input.txt', 'r') as file:
    lines = file.readlines()
    #lines = [line.rstrip() for line in lines] Cette ligne fausse le nombre d'espace en bout de ligne

columns = 9 #Dans l'idéal cette valeur devrait être calculée... 
columnsList = [[] for i in range(columns)]
instruction = []
stacks = []

for line in lines: 

    if line == '\n':
        break
    for i, j in zip(range(1, columns * 4 - 1, 4), range(columns)): #Itère à la fois sur les caractères de la ligne et sur les tableaux 
        if line[i] != " " and ord(line[i]) > 57: #Supprime les caractères numériques en se basant sur la valeur ASCII
            columnsList[j].append(line[i])


for line in lines: 
    instruction.append(line)

    if line.strip() == "":
        instruction = []

moveorder = []
for line in instruction:
    moveorder.append([int(s) for s in re.findall(r'\b\d+\b', line)]) #https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
   
    
for tab in moveorder:
    numberofcrates = tab[0]
    departstack = tab[1]
    arrivalstack = tab[2]
    
    cratestomove = columnsList[departstack -1][0:numberofcrates] #On ajoute -1 car la liste des colonnes démarre à 0
    cratestomove.reverse()

    
    for i in range(len(cratestomove)):
        columnsList[departstack -1].remove(cratestomove[i])
        columnsList[arrivalstack -1][:0] = cratestomove[i]
    

def Extract(lst): #
    return [item[0] for item in lst]

print(''.join(Extract(columnsList)))

