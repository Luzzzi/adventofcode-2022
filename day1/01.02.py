with open('input.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    
lines.append("")

print(lines)

mostCalories = 0
sum = 0
elves = []
sumbyelve = 0

for i in range(len(lines)): 
    if lines[i].strip() != "":
        sum += int(lines[i])
        
        if sum > mostCalories:
            mostCalories = sum
        if sum > sumbyelve: 
            print("la somme", sum)
            sumbyelve = sum

    else:
        print("je suis la somme de l'elfe", sumbyelve)
        elves.append(sumbyelve) ## Ne fonctionne pas pour les derniers tours de boucles puisque passe dans la première condition
        sumbyelve = 0
        sum = 0

elves_sorted = sorted(elves, reverse=True)
print(elves_sorted)
result = elves_sorted[0] + elves_sorted[1] + elves_sorted[2]
print(result)

print("L'elfe qui porte le maximum de calories porte :", mostCalories)

