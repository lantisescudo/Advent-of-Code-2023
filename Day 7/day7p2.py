import functools

def handcompare(handset1,handset2):
    cardranks = ["J","2","3","4","5","6","7","8","9","T","Q","K","A"]
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

    cards = {}
    for char in pair[0]:
        cards[char] = cards.get(char,0) + 1

    print(max(cards.values()))
    print(cards.get('J'))

    if (len(cards) == 1):
        hands['fiveofakinds'].append((pair[0],int(pair[1])))
    elif (len(cards) == 2):
        if ((max(cards.values()) == 4) and ((cards.get('J') == 4) or (cards.get('J') == 1))):
            hands['fiveofakinds'].append((pair[0],int(pair[1])))
        elif (max(cards.values()) == 4):
            hands['fourofakinds'].append((pair[0],int(pair[1])))
        elif ((cards.get('J') == 3) or (cards.get('J') == 2)):
            hands['fiveofakinds'].append((pair[0],int(pair[1])))
        else:
            hands['fullhouse'].append((pair[0],int(pair[1])))
    elif (len(cards) == 3):
        if ((max(cards.values()) == 3) and (cards.get('J') == 3)):
            hands['fourofakinds'].append((pair[0],int(pair[1])))
        elif ((max(cards.values()) == 3) and (cards.get('J') == 1)):
            hands['fourofakinds'].append((pair[0],int(pair[1])))
        elif (max(cards.values()) == 3):
            print(cards.get('J'))
            hands['threeofakind'].append((pair[0],int(pair[1])))
        elif ((max(cards.values()) == 2) and (cards.get('J') == 2)):
            hands['fourofakinds'].append((pair[0],int(pair[1])))
        elif ((max(cards.values()) == 2) and (cards.get('J') == 1)):
            hands['fullhouse'].append((pair[0],int(pair[1])))
        else:
            hands['twopair'].append((pair[0],int(pair[1])))
    elif (len(cards) == 4):
        if ((max(cards.values()) == 2) and (cards.get('J') == 2)):
            hands['threeofakind'].append((pair[0],int(pair[1])))
        elif ((max(cards.values()) == 2) and (cards.get('J') == 1)):
            hands['threeofakind'].append((pair[0],int(pair[1])))
        else:
            hands['onepair'].append((pair[0],int(pair[1])))
    elif (len(cards) == 5):
        if (cards.get('J') == 1):
            hands['onepair'].append((pair[0],int(pair[1])))
        else:
            hands['highcard'].append((pair[0],int(pair[1])))

    # cards = sorted(pair[0])
    # cnt = cards.count(cards[0])
    # jokers = cards.count("J")
    # if ((cnt == 5) or ((cnt == 4) and (jokers == 1)) or ((cnt == 4) and (jokers == 4)) or ((cnt == 3) and (jokers == 2)) or ((cnt == 2) and (jokers == 3)) or ((cnt == 1) and (jokers == 4))):
    #     hands['fiveofakinds'].append((pair[0],int(pair[1])))
    # elif (cnt == 4):
    #     hands['fourofakinds'].append((pair[0],int(pair[1])))
    # elif (cnt == 3):
    #     if (jokers == 3):
    #         if (cards[3] == cards[4]):
    #             hands['fiveofakinds'].append((pair[0],int(pair[1])))
    #         else:
    #             hands['fourofakinds'].append((pair[0],int(pair[1])))
    #     elif (jokers == 1):
    #         hands['fourofakinds'].append((pair[0],int(pair[1])))
    #     elif (cards[3] == cards[4]):
    #         hands['fullhouse'].append((pair[0],int(pair[1])))
    #     else:
    #         hands['threeofakind'].append((pair[0],int(pair[1])))
    # elif (cnt == 2):
    #     if ((cards[2] == cards[3]) and (cards[3] == cards[4])):
    #         if (jokers == 2):
    #             hands['fiveofakinds'].append((pair[0],int(pair[1])))
    #         else:
    #             hands['fullhouse'].append((pair[0],int(pair[1])))
    #     elif ((cards[2] == cards[3]) or (cards[3] == cards[4])):
    #         if (jokers == 2):
    #             hands['fourofakinds'].append((pair[0],int(pair[1])))
    #         elif (jokers == 1):
    #             hands['fullhouse'].append((pair[0],int(pair[1])))
    #         else:
    #             hands['twopair'].append((pair[0],int(pair[1])))
    #     else:
    #         if (jokers == 2):
    #             hands['threeofakind'].append((pair[0],int(pair[1])))
    #         elif(jokers == 1):
    #             hands['threeofakind'].append((pair[0],int(pair[1])))
    #         else:
    #             hands['onepair'].append((pair[0],int(pair[1])))
    # else:
    #     cnt = cards.count(cards[1])
    #     if (cnt == 4):
    #         hands['fourofakinds'].append((pair[0],int(pair[1])))
    #     elif (cnt == 3):
    #         if (jokers == 3):
    #             hands['fourofakinds'].append((pair[0],int(pair[1])))
    #         elif (jokers == 1):
    #             hands['fourofakinds'].append((pair[0],int(pair[1])))
    #         else:
    #             hands['threeofakind'].append((pair[0],int(pair[1])))
    #     elif (cnt == 2):
    #         if (cards[3] == cards[4]):
    #             if (jokers == 2):
    #                 hands['fourofakinds'].append((pair[0],int(pair[1])))
    #             elif (jokers == 1):
    #                 hands['fullhouse'].append((pair[0],int(pair[1])))
    #             else:
    #                 hands['twopair'].append((pair[0],int(pair[1])))
    #         else:
    #             if (jokers == 2):
    #                 hands['threeofakind'].append((pair[0],int(pair[1])))
    #             elif (jokers == 1):
    #                 hands['threeofakind'].append((pair[0],int(pair[1])))
    #             else:
    #                 hands['onepair'].append((pair[0],int(pair[1])))
    #     else:
    #         cnt = cards.count(cards[2])
    #         if (cnt == 3):
    #             if (jokers == 3):
    #                 hands['fourofakinds'].append((pair[0],int(pair[1])))
    #             elif (jokers == 1):
    #                 hands['fourofakinds'].append((pair[0],int(pair[1])))
    #             else:
    #                 hands['threeofakind'].append((pair[0],int(pair[1])))
    #         elif (cnt == 2):
    #             if (jokers == 2):
    #                 hands['threeofakind'].append((pair[0],int(pair[1])))
    #             elif (jokers == 1):
    #                 hands['threeofakind'].append((pair[0],int(pair[1])))
    #             else:
    #                 hands['onepair'].append((pair[0],int(pair[1])))
    #         else:
    #             cnt = cards.count(cards[3])
    #             if (cnt == 2):
    #                 if (jokers == 2):
    #                     hands['threeofakind'].append((pair[0],int(pair[1])))
    #                 elif (jokers == 1):
    #                     hands['threeofakind'].append((pair[0],int(pair[1])))
    #                 else:
    #                     hands['onepair'].append((pair[0],int(pair[1])))
    #             else:
    #                 if (jokers == 2):
    #                     hands['threeofakind'].append((pair[0],int(pair[1])))
    #                 elif (jokers == 1):
    #                     hands['onepair'].append((pair[0],int(pair[1])))
    #                 else:
    #                     hands['highcard'].append((pair[0],int(pair[1])))

rank = 0
score = 0

keylist = ['highcard','onepair','twopair','threeofakind','fullhouse','fourofakinds','fiveofakinds']
write = open("p7check.txt","w")

for key in keylist:
    list = sorted(hands[key],key=functools.cmp_to_key(handcompare))
    write.write(key + "\n")
    for item in list:
        write.write(item[0] + "," + ''.join(sorted(item[0])) + "," + str(item[1]) + "\n")
    # print(list)
    # print(len(list))
    for h in list:
        rank = rank + 1
        score = score + (rank * h[1])

print(score)
