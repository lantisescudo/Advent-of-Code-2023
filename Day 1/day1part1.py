nums = []
src = open("day1full.txt","r")

for line in src:
    first = None
    last = None
    for char in line:
        try:
            first = int(char)
            break
        except ValueError:
            "do nothing"
    
    for char in line[::-1]:
        try:
            last = int(char)
            break
        except ValueError:
            "do nothing"
    
    nums.append((first*10)+last)

solution = 0
for item in nums:
    solution = solution + item

print(solution)
"Wait"