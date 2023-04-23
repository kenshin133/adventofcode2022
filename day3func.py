def splitInput(input):
    compartments=[]
    compartments.append(input[0:len(input)//2])
    compartments.append(input[len(input)//2:])
    return compartments

def findCommon(side1,side2):
    for _ in side1:
        if _ in side2:
            #print(_)
            return _

def find3Common(side1,side2,side3):
    for _ in side1:
        if _ in side2:
            if _ in side3:
                print(_)
                return _

def findPriority(letter):
    #Lowercase item types a through z have priorities 1 through 26.
    #Uppercase item types A through Z have priorities 27 through 52.
    if letter.islower():
        #print(f'{letter} is index {ord(letter) - 96}')
        return ord(letter) - 96
    else:
        #print(f'{letter} is sindex {ord(letter) - 38}')
        #print({ord(letter) - 38})
        return ord(letter) - 38

def GroupMultiple(groupOfItems, numberOfGrouped):
    tick = 0
    newGroupOfItems = []
    temp = []

    for item in groupOfItems:
        #we get in an array, we want to return an array of arrays containing 3 each?
        tick = tick + 1
        temp.append(item.replace('\n',''))
        if tick == 3:
            newGroupOfItems.append(temp)
            tick = 0
            temp = []
    return newGroupOfItems
