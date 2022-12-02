with open('input.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


# StrategyGuides: 
# X = Loose
# Y = draw
# Z = Win 

# For Player 1 :
# A = Rock
# B = Paper
# C = Scissors

win = 6
draw = 3
rock = 1
paper = 2
scissors = 3

score = 0 

def ScoreByShape(player1, score):
    if player1 == "A":
        score += scissors
    elif player1 == "B":
        score += rock 
    elif player1 == "C":
        score += paper
    return score



for line in lines:
    round = line.split()
    player1 = round[0]
    gamestrategy = round[1]

    if gamestrategy == "X": #Je dois perdre
        if player1 == "A":
            score += scissors
        elif player1 == "B":
            score += rock 
        elif player1 == "C":
            score += paper
        
    elif gamestrategy  == "Y": #Je dois égalité
        score += draw
        if player1 == "A":
            score += rock
        elif player1 == "B":
            score += paper
        elif player1 == "C":
            score += scissors
     
    elif gamestrategy == "Z": # Je dois gagner
        score += win
        if player1 == "A":
            score += paper
        elif player1 == "B":
            score += scissors
        elif player1 == "C":
            score += rock
        

print(score)