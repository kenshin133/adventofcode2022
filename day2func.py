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
def givescore(shape):
    if shape == 'Y':
        return 2
    if shape == 'X':
        return 1
    if shape == 'Z':
        return 3