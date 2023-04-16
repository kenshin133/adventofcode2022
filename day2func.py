def iswin(move):
    theirmove=move[0]
    mymove=move[1]
    print(theirmove,mymove)
    if theirmove == "A":
        if mymove != "Y":
            return 0
        else:
            return 1
    if theirmove == "B":
        if mymove != "Z":
            return 0
        else:
            return 1
    if theirmove == "C":
        if mymove != "X":
            return 0
        else:
            return 1

def istie(move):
    theirmove=move[0]
    mymove=move[1]
    print(theirmove,mymove)
    if theirmove == "A":
        if mymove != "X":
            return 0
        else:
            return 1
    if theirmove == "B":
        if mymove != "Y":
            return 0
        else:
            return 1
    if theirmove == "C":
        if mymove != "Z":
            return 0
        else:
            return 1

def istie2(move):
    outcome=move[1]
    if outcome == "Y":
        return 1
    else:
        return 0

def iswin2(move):
    theirmove=move[0]
    outcome=move[1]
    if outcome == "Z":
        return 1
    else:
        return 0

def givescore(shape):
    if shape == 'Y':
        return 2
    if shape == 'X':
        return 1
    if shape == 'Z':
        return 3

def getScore(lose, tie, won, move):
    if won == 1:
        if move == "A":
            return 2
        if move == "B":
            return 3
        if move == "C":
            return 1
    elif tie == 1:
        if move == "A":
            return 1
        if move == "B":
            return 2
        if move == "C":
            return 3
    else:
        if move == "A":
            return 3
            print("set score to 3")
        if move == "B":
            return 1
            print("set score to 1")
        if move == "C":
            return 2