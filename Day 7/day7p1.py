import functools

def handcompare(handset1,handset2):
    cardranks = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
    hand1 = handset1[0]
    hand2 = handset2[0]
    idx = 0
    while True:
        if (hand1[idx] == hand2[idx]):
            idx = idx + 1
        else:
            if cardranks.index(hand1[idx]) > cardranks.index(hand2[idx]):
                return 1
            else:
                return -1

src = open("C:\\Users\\Lantis\\Documents\\GitHub\\Advent-of-Code-2023\\Day 7\\day7full.txt","r")

hands = {
    'fiveofakinds': [],
    'fourofakinds': [],
    'fullhouse': [],
    'threeofakind': [],
    'twopair': [],
    'onepair': [],
    'highcard': []
}

for line in src:
    pair = line.split()
    cards = sorted(pair[0])
    cnt = cards.count(cards[0])
    if (cnt == 5):
        hands['fiveofakinds'].append((pair[0],int(pair[1])))
    elif (cnt == 4):
        hands['fourofakinds'].append((pair[0],int(pair[1])))
    elif (cnt == 3):
        if (cards[3] == cards[4]):
            hands['fullhouse'].append((pair[0],int(pair[1])))
        else:
            hands['threeofakind'].append((pair[0],int(pair[1])))
    elif (cnt == 2):
        if ((cards[2] == cards[3]) and (cards[3] == cards[4])):
            hands['fullhouse'].append((pair[0],int(pair[1])))
        elif ((cards[2] == cards[3]) or (cards[3] == cards[4]) or (cards[2] == cards[4])):
            hands['twopair'].append((pair[0],int(pair[1])))
        else:
            hands['onepair'].append((pair[0],int(pair[1])))
    else:
        cnt = cards.count(cards[1])
        if (cnt == 4):
            hands['fourofakinds'].append((pair[0],int(pair[1])))
        elif (cnt == 3):
            hands['threeofakind'].append((pair[0],int(pair[1])))
        elif (cnt == 2):
            if (cards[3] == cards[4]):
                hands['twopair'].append((pair[0],int(pair[1])))
            else:
                hands['onepair'].append((pair[0],int(pair[1])))
        else:
            cnt = cards.count(cards[2])
            if (cnt == 3):
                hands['threeofakind'].append((pair[0],int(pair[1])))
            elif (cnt == 2):
                hands['onepair'].append((pair[0],int(pair[1])))
            else:
                cnt = cards.count(cards[3])
                if (cnt == 2):
                    hands['onepair'].append((pair[0],int(pair[1])))
                else:
                    hands['highcard'].append((pair[0],int(pair[1])))

rank = 0
score = 0

keylist = ['highcard','onepair','twopair','threeofakind','fullhouse','fourofakinds','fiveofakinds']

for key in keylist:
    for h in sorted(hands[key],key=functools.cmp_to_key(handcompare)):
        rank = rank + 1
        score = score + (rank * h[1])

print(score)