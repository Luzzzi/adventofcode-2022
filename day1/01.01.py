with open('input.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

mostCalories = 0
sum = 0

for line in lines: 
    if line.strip() != "":
        sum += int(line)
        
        if sum > mostCalories:
            mostCalories = sum

    else:
        sum = 0

print("L'elfe qui porte le maximum de calories porte :", mostCalories)

