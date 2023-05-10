file=open("day5-input","r")

temp=file.readlines()
from day5func import *

# '''example 
#         [D]    
#     [N] [C]    
#     [Z] [M] [P]
#     1   2   3 

#     move 1 from 2 to 1
#     move 3 from 1 to 3
#     move 2 from 2 to 1
#     move 1 from 1 to 2

#     In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

#     The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

# '''


stacks = getBoxesFromInput(temp)
directions = getDirections(temp)
for direction in directions:
    quantity,frompile,topile = parseDirection(direction)
    moveBetweenStacks(stacks,quantity,frompile,topile)


renderStacks(stacks)
growArray(stacks)
#write the file, replace this with a proper rendering
#for i in temp:
#    print(i.replace('\n',''))

#TODO Add method to give output..
print("the results from sample should be\n        [Z]\n        [N]\n        [D]\n[C] [M] [P]\n 1   2   3")

