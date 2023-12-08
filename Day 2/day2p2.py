import re

nums = []
src = open("C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2023\\Day 2\\day2full.txt","r")
pattern = re.compile("Game (\d+): (.*)")

for line in src:
    match = re.search(pattern,line)
    id = int(match.group(1))
    games = match.group(2)
    min_red = 0
    min_green = 0
    min_blue = 0

    batches = games.split('; ')

    for b in batches:
        sets = b.split(', ')

        for s in sets:
            count, color = s.split(' ')
            count = int(count)

            if ((color == "red") and (count > min_red)):
                min_red = count

            if ((color == "green") and (count > min_green)):
                min_green = count

            if ((color == "blue") and (count > min_blue)):
                min_blue = count
    
    power = min_red * min_green * min_blue
    nums.append(power)

sum = 0
for item in nums:
    sum = sum + item

print(sum)

"Wait"