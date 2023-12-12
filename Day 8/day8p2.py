import re
import math

src = open("C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2023\\Day 8\\day8full.txt","r")

directions = src.readline().strip()
dirpos = 0
currpos = []
steps = 0

nodes = {}
pattern = "(\w+) = \((\w+), (\w+)\)"

for line in src:
    match = re.search(pattern,line)
    if match:
        nodes[match.group(1)] = (match.group(2),match.group(3))
        if (match.group(1)[2] == "A"):
            currpos.append(match.group(1))

steps = []
for n in currpos:
    thisstep = 0
    dirpos = 0
    currplace = n
    nextstep = True
    while nextstep:
        thisstep += 1
        if (directions[dirpos] == "L"):
            turn = 0
        else:
            turn = 1

        n = nodes[n][turn]

        if (n[2] == "Z"):
            nextstep = False

        dirpos += 1
        if (dirpos == len(directions)):
            dirpos = 0
    
    steps.append(thisstep)

print(math.lcm(*steps))

"wait"