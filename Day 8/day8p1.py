import re

src = open("C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2023\\Day 8\\day8full.txt","r")

directions = src.readline().strip()
dirpos = 0
currpos = "AAA"
steps = 0

nodes = {}
pattern = "(\w+) = \((\w+), (\w+)\)"

for line in src:
    match = re.search(pattern,line)
    if match:
        nodes[match.group(1)] = (match.group(2),match.group(3))

while (currpos != "ZZZ"):
    steps += 1
    if (directions[dirpos] == "L"):
        currpos = nodes[currpos][0]
    else:
        currpos = nodes[currpos][1]
    
    dirpos += 1
    if (dirpos == len(directions)):
        dirpos = 0

print(steps)

"wait"