def getBoxesFromInput(text):
    #i think this would be much easier if I had oriented the arrays sideways, to where each column is its own array
    #basically try to get the initial text into an array, gathering spaces into groups of 3 seperated by 1 space or nothing(if beginning or end)
   
    bigarray=[]
    for row in text:
        smallarray=[]
        previous="NULL"

        if any(char.isdigit() for char in row):
            break
        else:
            numberofspace=0
            skip=0    
            for column in row.replace('\n','').replace('[','').replace(']',''):
                if skip==1:
                    skip=0
                    #print(f"skipping {column}")
                    pass
                else:
                    if column == ' ':
                        numberofspace=numberofspace+1
                        #print(f'number of spaces {numberofspace}')
                        if numberofspace == 3:
                            smallarray.append(column)
                            numberofspace=0
                            #print("adding a space to the array")
                            skip=1
                    else:
                        smallarray.append(column)
                        numberofspace=0
                        skip=0

        #print(smallarray)
        bigarray.append(smallarray)
    return bigarray
    #goal is an array that looks like of like : 
    #[ ][d][ ]
    #[n][c][ ] but maybe it could be turnes sideways? 
    #[z][m][p]


def renderStacks(stacks):
    for i in stacks:
        print(i)


def moveBetweenStacks(stacks,quantity,fromStack,toStack):
    for i in range(0,quantity):
        grabBox=grabTopBox(stacks,fromStack)
        #print(getTopBox(stacks,1))
        #print(grabBox,grabBoxIndex)
        placeBoxs(stacks,grabBox,toStack)


def moveMultipleBetweenStacks(stacks,quantity,fromStack,toStack):
    boxes=[]
    for i in range(0,quantity):
        boxes.append(grabTopBox(stacks,fromStack))
        #print(boxes)
        print(f"something {boxes}")
    placeBoxs(stacks,boxes,toStack)


def grabTopBox(stacks,stackNumber):

    pos=0
    lastempty=0
    for j in stacks:
        
        #-1 so we can shift the position from 1-3 to 0-2
        if j[stackNumber-1] == " ":
            #print("space")
            lastempty=lastempty+1
        else:
            #print(f'[{j[stackNumber-1]}]')
            #print(pos)
            lastvalue=j[stackNumber-1]
            (stacks[pos][stackNumber-1]) = " "
            #print(j)
            return lastvalue
            break
        pos=pos+1
        #print(f" pos is : {pos} and lastempty is {lastempty}")


def placeBox(stacks,boxValue,toStack):
    toIndex=getTopEmpty(stacks, toStack -1)
    #print(toIndex)
    #print(f'to stack : {toStack} {toIndex}')
    stacks[toIndex][toStack -1] = boxValue
    
    
def placeBoxs(stacks,boxes,toStack):
    index=1
    print(boxes)
    if len(boxes) != 1: 
        boxes.reverse()
        print(boxes)
        for boxValue in boxes:
            toIndex=getTopEmpty(stacks, toStack -1)
            #print(toIndex)
            #print(f'to stack : {toStack} {toIndex}')
            stacks[toIndex][toStack -1] = boxValue[0]
            index + 1
    else:
        toIndex=getTopEmpty(stacks, toStack -1)
        #print(toIndex)
        #print(f'to stack : {toStack} {toIndex}')
        stacks[toIndex][toStack -1] = boxes[0]
        index + 1


def getTopEmpty(stacks,stacktoaddto):
    lastempty=0
    pos=0
    for j in stacks:
        if j[stacktoaddto] != " " and pos == 0:
            growArray(stacks)
            return lastempty
        elif j[stacktoaddto] == " " and pos == len(stacks) -1:
            return len(stacks) -1
            break
        elif j[stacktoaddto] != " ":
            pos = pos + 1
            return lastempty - 1
        elif j[stacktoaddto] == " ":
            lastempty = lastempty + 1
            pos = pos + 1
        else:
            break
    #print(f'pos : {pos}')
    return lastempty


def growArray(stacks):
    for i in stacks[0]:
        
        if i != " ":
            temparray=[]
            finalArray=[]
            #make top column
            
            
            for d in range(0,len(stacks[0])):
                ar=" "
                temparray.append(ar)
                #print(temparray)
            stacks.insert(0,temparray)


def getDirections(lines):
    #print(lines)
    #['    [D]    \n', '[N] [C]    \n', '[Z] [M] [P]\n', ' 1   2   3 \n', '\n', 'move 1 from 2 to 1\n', 'move 3 from 1 to 3\n', 'move 2 from 2 to 1\n', 'move 1 from 1 to 2']
    #is the input, split out usable arrays from the end
    rules=[]
    for i in lines:
        if "move" in i:
            #print(i)
            rules.append(i)
            #print(rules)
    return rules


def parseDirection(direction):
    print(direction)
    direction=direction.split(" ")
    print(f'returning {direction[1]},{direction[3]},{direction[5]}')    
    return int(direction[1]),int(direction[3]),int(direction[5])