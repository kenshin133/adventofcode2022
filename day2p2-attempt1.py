file=open("day2-input","r")

temp=file.readlines()
from day2func import *

# '''For example, suppose you were given the following strategy guide:

# A Y
# B X
# C Z
# The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

# In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
# In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
# In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.'''


moves=[]
totalscore=0
#get rid of newlines, turn into list of lists.
for i in range(0,len(temp)):
    moves.append(temp[i].replace('\n', '').split(' '))

for move in moves:
    won=0
    tie=0
    lose=0
    score=0
    if iswin2(move):
        won=1
        print(str(move) + "won")
        score=6
    elif istie2(move):
        tie=1
        print(str(move) + "tied")
        score=3
    else:
        lose=1
        print(str(move) + "lost")
        score=0
    score = score + getScore(lose, tie, won, move[0])
    print(f"your score is {score}")
    totalscore=totalscore+score
print(f"your totalscore is {totalscore}")
print("the sample answer should be 12")