src = open("C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2023\\Day 6\\day6full.txt","r")

line = src.readline()
times = line.split()
line = src.readline()
distances = line.split()

races = []
for i in range(1,len(times)):
    races.append([int(times[i]),int(distances[i])])

wins = []
for r in races:
    wincount = 0
    time = r[0]
    for i in range(time):
        distance = i * (time-i)
        if (distance > r[1]):
            wincount = wincount + 1
    
    wins.append(wincount)

score = 1
for w in wins:
    score = score * w

print(score)

"Wait"