src = open("C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2023\\Day 3\\day3full.txt","r")

rows = []
for line in src:
    rows.append(line.strip())

walking = True
partnums = []
x_pos = 0
y_pos = 0
currval = 0
adjacent = False

while walking:
    char = rows[x_pos][y_pos]
    if ((char < '0') or (char > '9')):
        if ((currval > 0) and adjacent):
            partnums.append(currval)

        currval = 0
        adjacent = False

        y_pos = y_pos + 1
        if (y_pos == len(rows[x_pos])):
            y_pos = 0
            x_pos = x_pos + 1
        if (x_pos == len(rows)):
            walking = False
        
        continue

    num = int(char)
    currval = (currval*10)+num
    if not adjacent:
        if (x_pos > 0):
            # Above
            testchar = rows[x_pos-1][y_pos]
            if (((testchar < '0') or (testchar > '9')) and (testchar != '.')):
                adjacent = True
            
            #Above-left
            if (y_pos > 0):
                testchar = rows[x_pos-1][y_pos-1]
                if (((testchar < '0') or (testchar > '9')) and (testchar != '.')):
                    adjacent = True

            #Above-right
            if (y_pos < len(rows[x_pos])-1):
                testchar = rows[x_pos-1][y_pos+1]
                if (((testchar < '0') or (testchar > '9')) and (testchar != '.')):
                    adjacent = True

        #Left
        if (y_pos > 0):
            testchar = rows[x_pos][y_pos-1]
            if (((testchar < '0') or (testchar > '9')) and (testchar != '.')):
                adjacent = True

        #Right
        if (y_pos < len(rows[x_pos])-1):
            testchar = rows[x_pos][y_pos+1]
            if (((testchar < '0') or (testchar > '9')) and (testchar != '.')):
                adjacent = True

        if (x_pos < len(rows)-1):
            # Below
            testchar = rows[x_pos+1][y_pos]
            if (((testchar < '0') or (testchar > '9')) and (testchar != '.')):
                adjacent = True
            
            #Below-left
            if (y_pos > 0):
                testchar = rows[x_pos+1][y_pos-1]
                if (((testchar < '0') or (testchar > '9')) and (testchar != '.')):
                    adjacent = True

            #Below-right
            if (y_pos < len(rows[x_pos])-1):
                testchar = rows[x_pos+1][y_pos+1]
                if (((testchar < '0') or (testchar > '9')) and (testchar != '.')):
                    adjacent = True

    y_pos = y_pos + 1
    if (y_pos == len(rows[x_pos])):
        y_pos = 0
        x_pos = x_pos + 1
    if (x_pos == len(rows)):
        if adjacent:
            partnums.append(currval)
        walking = False

sum = 0
for item in partnums:
    sum = sum + item

print(sum)
"Wait"