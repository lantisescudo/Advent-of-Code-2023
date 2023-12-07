import re

src = open("C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2023\\Day 5\\day5full.txt","r")
pattern = re.compile("(\w+-to-\w+) map:")

seedsoil = []
soilfert = []
fertwater = []
waterlight = []
lighttemp = []
temphumid = []
humidloc = []

for line in src:
    if (line.strip() == ""):
        continue
    
    if (line[:6] == "seeds:"):
        seeds = list(map(int,line.split()[1:]))
        continue

    match = re.search(pattern,line)
    if (match != None):
        maptype = match.group(1)
        continue

    #is a mapping
    set = list(map(int,line.split()))
    if (maptype == "seed-to-soil"):
        seedsoil.append(set)
    elif (maptype == "soil-to-fertilizer"):
        soilfert.append(set)
    elif (maptype == "fertilizer-to-water"):
        fertwater.append(set)
    elif (maptype == "water-to-light"):
        waterlight.append(set)
    elif (maptype == "light-to-temperature"):
        lighttemp.append(set)
    elif (maptype == "temperature-to-humidity"):
        temphumid.append(set)
    elif (maptype == "humidity-to-location"):
        humidloc.append(set)

locations = []

for s in seeds:
    dest = s
    for map in seedsoil:
        if ((dest >= map[1]) and (dest < (map[1] + map[2]))):
            offset = dest - map[1]
            dest = map[0] + offset
            break
    for map in soilfert:
        if ((dest >= map[1]) and (dest < (map[1] + map[2]))):
            offset = dest - map[1]
            dest = map[0] + offset
            break
    for map in fertwater:
        if ((dest >= map[1]) and (dest < (map[1] + map[2]))):
            offset = dest - map[1]
            dest = map[0] + offset
            break
    for map in waterlight:
        if ((dest >= map[1]) and (dest < (map[1] + map[2]))):
            offset = dest - map[1]
            dest = map[0] + offset
            break
    for map in lighttemp:
        if ((dest >= map[1]) and (dest < (map[1] + map[2]))):
            offset = dest - map[1]
            dest = map[0] + offset
            break
    for map in temphumid:
        if ((dest >= map[1]) and (dest < (map[1] + map[2]))):
            offset = dest - map[1]
            dest = map[0] + offset
            break
    for map in humidloc:
        if ((dest >= map[1]) and (dest < (map[1] + map[2]))):
            offset = dest - map[1]
            dest = map[0] + offset
            break
    
    locations.append(dest)

print(min(locations))

"Wait"
