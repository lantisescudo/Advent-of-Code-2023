import re

src = open("C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2023\\Day 4\\day4full.txt","r")

score = 0

for line in src:
    wins = set()
    have = []
    parse = re.split(r'[:|]',line)
    for item in parse[1].split():
        wins.add(int(item))
    
    for item in parse[2].split():
        have.append(int(item))
    
    count = 0
    for item in have:
        if item in wins:
            count = count + 1
    
    if (count > 0):
        score = score + (2**(count-1))

print(score)
"Wait"