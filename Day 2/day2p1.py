import re

nums = []
src = open("C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2023\\Day 2\\day2full.txt","r")
pattern = re.compile("Game (\d+): (.*)")

for line in src:
    match = re.search(pattern,line)
    id = int(match.group(1))
    games = match.group(2)
    possible = True

    batches = games.split('; ')

    for b in batches:
        if not possible:
            break
        sets = b.split(', ')

        for s in sets:
            count, color = s.split(' ')
            count = int(count)

            if ((color == "red") and (count > 12)):
                possible = False
                break
            if ((color == "green") and (count > 13)):
                possible = False
                break
            if ((color == "blue") and (count > 14)):
                possible = False
                break
    
    if possible:
        nums.append(id)

sum = 0
for item in nums:
    sum = sum + item

print(sum)

"Wait"