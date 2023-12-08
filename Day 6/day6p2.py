src = open("C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2023\\Day 6\\day6full.txt","r")

line = src.readline()
times = line.split()
line = src.readline()
distances = line.split()

timestr = ""
diststr = ""

for i in range(1,len(times)):
    timestr = timestr + times[i]
    diststr = diststr + distances[i]

finaltime = int(timestr)
finaldist = int(diststr)

wincount = 0
for i in range(finaltime):
    distance = i * (finaltime-i)
    if (distance > finaldist):
        wincount = wincount + 1
    
print(wincount)

"Wait"