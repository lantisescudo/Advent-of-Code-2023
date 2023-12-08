import re

src = open("C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2023\\Day 4\\day4full.txt","r")

cards = []

for line in src:
    wins = set()
    have = []
    parse = re.split(r'[:|]',line)
    for item in parse[1].split():
        wins.add(int(item))
    
    for item in parse[2].split():
        have.append(int(item))
    
    cards.append([wins,have,1])

for c in range(len(cards)):
    count = cards[c][2]
    wincount = 0
    for item in cards[c][1]:
        if item in cards[c][0]:
            wincount = wincount + 1

    if (wincount > 0):
        for i in range(wincount):
            cards[c+i+1][2] = cards[c+i+1][2] + count

sum = 0
for c in cards:
    sum = sum + c[2]

print(sum)

"Wait"