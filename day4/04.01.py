with open('input.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

pairs = 0 

for line in lines:
    elves = line.split(',')
    firstsection = elves[0].split("-")
    secondsection = elves[1].split("-")

    if (int(firstsection[0]) <= int(secondsection[0]) and int(firstsection[1]) >= int(secondsection[1])) or (int(secondsection[0]) <= int(firstsection[0]) and int(secondsection[1]) >= int(firstsection[1])):
        pairs += 1
        print(elves)

print(pairs)