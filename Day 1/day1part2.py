nums = []
src = open("day1full.txt","r")

for line in src:
    first = None
    last = None
    for pos in range(len(line)):
        try:
            first = int(line[pos])
            break
        except ValueError:
            if (line[pos:pos+3] == "one"):
                first = 1
                break
            elif (line[pos:pos+3] == "two"):
                first = 2
                break
            elif (line[pos:pos+5] == "three"):
                first = 3
                break
            elif (line[pos:pos+4] == "four"):
                first = 4
                break
            elif (line[pos:pos+4] == "five"):
                first = 5
                break
            elif (line[pos:pos+3] == "six"):
                first = 6
                break
            elif (line[pos:pos+5] == "seven"):
                first = 7
                break
            elif (line[pos:pos+5] == "eight"):
                first = 8
                break
            elif (line[pos:pos+4] == "nine"):
                first = 9
                break

    
    for pos in range(len(line)-1,-1,-1):
        try:
            last = int(line[pos])
            break
        except ValueError:
            val = line[pos-2:pos+1]
            if (line[pos-2:pos+1] == "one"):
                last = 1
                break
            elif (line[pos-2:pos+1] == "two"):
                last = 2
                break
            elif (line[pos-4:pos+1] == "three"):
                last = 3
                break
            elif (line[pos-3:pos+1] == "four"):
                last = 4
                break
            elif (line[pos-3:pos+1] == "five"):
                last = 5
                break
            elif (line[pos-2:pos+1] == "six"):
                last = 6
                break
            elif (line[pos-4:pos+1] == "seven"):
                last = 7
                break
            elif (line[pos-4:pos+1] == "eight"):
                last = 8
                break
            elif (line[pos-3:pos+1] == "nine"):
                last = 9
                break
    
    nums.append((first*10)+last)

solution = 0
for item in nums:
    solution = solution + item

print(solution)
"Wait"