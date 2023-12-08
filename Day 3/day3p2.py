src = open("C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2023\\Day 3\\day3full.txt","r")

rows = []
for line in src:
    rows.append(line.strip())

gears = []

for x in range(len(rows)):
    for y in range(len(rows[x])):
        if (rows[x][y] == '*'):
            gears.append((x,y))

powers = []

for g in gears:
    nums = []
    x_pos = g[0]
    y_pos = g[1]

    #Check left
    if (y_pos > 0):
        y_start = y_pos-1
        testchar = rows[x_pos][y_start]
        num = None
        while (num == None):
            if ((testchar >= '0') and (testchar <= '9')):
                if (y_start == 0):
                    y_start = y_start-1
                else:
                    y_start = y_start-1
                    testchar = rows[x_pos][y_start]
                    continue

            y_start = y_start+1
            if (y_start == y_pos):
                break

            num = int(rows[x_pos][y_start:y_pos])
            nums.append(num)

    #Check right
    if (y_pos > 0):
        y_end = y_pos+1
        testchar = rows[x_pos][y_end]
        num = None
        while (num == None):
            if ((testchar >= '0') and (testchar <= '9')):
                if (y_end == len(rows[x_pos])-1):
                    y_end = y_end+1
                else:
                    y_end = y_end+1
                    testchar = rows[x_pos][y_end]
                    continue

            y_end = y_end - 1
            if (y_end == y_pos):
                break

            num = int(rows[x_pos][y_pos+1:y_end+1])
            nums.append(num)

    #Check Above
    if (x_pos != 0):
        x_check = x_pos - 1
        testchar = rows[x_check][y_pos]
        #Directly above
        if ((testchar >= '0') and (testchar <= '9')):
            y_start = y_pos - 1
            testchar = rows[x_check][y_start]
            walking = True
            while (walking):
                if ((testchar >= '0') and (testchar <= '9')):
                    if (y_start == 0):
                        walking = False
                    else:
                        y_start = y_start - 1
                        testchar = rows[x_check][y_start]
                else:
                    y_start = y_start + 1
                    walking = False
            
            y_end = y_pos + 1
            testchar = rows[x_check][y_end]
            walking = True
            while (walking):
                if ((testchar >= '0') and (testchar <= '9')):
                    if (y_end == len(rows[x_check])-1):
                        walking = False
                    else:
                        y_end = y_end + 1
                        testchar = rows[x_check][y_end]
                else:
                    y_end = y_end - 1
                    walking = False
            
            num = int(rows[x_check][y_start:y_end+1])
            nums.append(num)
        
        else:
            #Above-left walk
            testchar = rows[x_check][y_pos-1]
            if ((testchar >= '0') and (testchar <= '9')):
                y_start = y_pos - 1
                testchar = rows[x_check][y_start]
                walking = True
                while (walking):
                    if ((testchar >= '0') and (testchar <= '9')):
                        if (y_start == 0):
                            walking = False
                        else:
                            y_start = y_start - 1
                            testchar = rows[x_check][y_start]
                    else:
                        y_start = y_start + 1
                        walking = False

                num = int(rows[x_check][y_start:y_pos])
                nums.append(num)

            #Above-right walk
            testchar = rows[x_check][y_pos+1]
            if ((testchar >= '0') and (testchar <= '9')):
                y_end = y_pos + 1
                testchar = rows[x_check][y_end]
                walking = True
                while (walking):
                    if ((testchar >= '0') and (testchar <= '9')):
                        if (y_end == len(rows[x_check])-1):
                            walking = False
                        else:
                            y_end = y_end + 1
                            testchar = rows[x_check][y_end]
                    else:
                        y_end = y_end - 1
                        walking = False
                
                num = int(rows[x_check][y_pos+1:y_end+1])
                nums.append(num)

#Check below
    if (x_pos != len(rows)-1):
        x_check = x_pos + 1
        testchar = rows[x_check][y_pos]
        #Directly below
        if ((testchar >= '0') and (testchar <= '9')):
            y_start = y_pos - 1
            testchar = rows[x_check][y_start]
            walking = True
            while (walking):
                if ((testchar >= '0') and (testchar <= '9')):
                    if (y_start == 0):
                        walking = False
                    else:
                        y_start = y_start - 1
                        testchar = rows[x_check][y_start]
                else:
                    y_start = y_start + 1
                    walking = False
            
            y_end = y_pos + 1
            testchar = rows[x_check][y_end]
            walking = True
            while (walking):
                if ((testchar >= '0') and (testchar <= '9')):
                    if (y_end == len(rows[x_check])-1):
                        walking = False
                    else:
                        y_end = y_end + 1
                        testchar = rows[x_check][y_end]
                else:
                    y_end = y_end - 1
                    walking = False
            val = rows[x_check][y_start:y_end+1]
            num = int(val)
            nums.append(num)
        
        else:
            #Below-left walk
            testchar = rows[x_check][y_pos-1]
            if ((testchar >= '0') and (testchar <= '9')):
                y_start = y_pos - 1
                testchar = rows[x_check][y_start]
                walking = True
                while (walking):
                    if ((testchar >= '0') and (testchar <= '9')):
                        if (y_start == 0):
                            walking = False
                        else:
                            y_start = y_start - 1
                            testchar = rows[x_check][y_start]
                    else:
                        y_start = y_start + 1
                        walking = False

                num = int(rows[x_check][y_start:y_pos])
                nums.append(num)

            #Below-right walk
            testchar = rows[x_check][y_pos+1]
            if ((testchar >= '0') and (testchar <= '9')):
                y_end = y_pos + 1
                testchar = rows[x_check][y_end]
                walking = True
                while (walking):
                    if ((testchar >= '0') and (testchar <= '9')):
                        if (y_end == len(rows[x_check])-1):
                            walking = False
                        else:
                            y_end = y_end + 1
                            testchar = rows[x_check][y_end]
                    else:
                        y_end = y_end - 1
                        walking = False
                
                num = int(rows[x_check][y_pos+1:y_end+1])
                nums.append(num)

    if (len(nums) == 2):
        pow = nums[0] * nums[1]
        powers.append(pow)

sum = 0
for p in powers:
    sum = sum + p

print(sum)

"Wait"
