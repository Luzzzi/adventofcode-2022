with open('input.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# For Player 1 :
# A = Rock
# B = Paper
# C = Scissors

# For Player 2 : 
# Y = Paper
# X= Rock
# Z = Scissors 

win = 6
draw = 3
rock = 1
paper = 2
scissors = 3

score = 0 

for line in lines:
    round = line.split()
    if round[0] == 'A' and round[1] == "Y": # Je gagne
        score += win
        score += paper
    elif round[0] == 'B' and round[1] == "Y": # égalité
        score += draw 
        score += paper
    elif round[0] == 'C' and round[1] == "Y": # Je perds
        score += paper
    elif round[0] == 'A' and round[1] == "X": # égalité
        score += draw 
        score += rock
    elif round[0] == 'B' and round[1] == "X": # Je perds
        score += rock 
    elif round[0] == 'C' and round[1] == "X": # Je gagne
        score += win 
        score += rock
    elif round[0] == 'A' and round[1] == "Z": # Je perds
        score += scissors
    elif round[0] == 'B' and round[1] == "Z": # Je gagne
        score += win
        score += scissors  
    elif round[0] == 'C' and round[1] == "Z":
        score += scissors
        score += draw

print(score)