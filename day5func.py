def getBoxesFromInput(text):
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
        grab=getTopBox(stacks,1)
        #print(getTopBox(stacks,1))

def getTopBox(stacks,stackNumber):
    for j in stacks:
        #-1 so we can shift the position from 1-3 to 0-2
        print(j[stackNumber-1])