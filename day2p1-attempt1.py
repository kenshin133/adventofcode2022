file=open("day2-input","r")

temp=file.readlines()

from day2func import *

# '''For example, suppose you were given the following strategy guide:

# A Y
# B X
# C Z
# This strategy guide predicts and recommends the following:

# In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
# In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
# The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

# What would your total score be if everything goes exactly according to your strategy guide?'''

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
    if iswin(move):
        won=1
        print(str(move) + "won")
        score=6
    elif istie(move):
        tie=1
        print(str(move) + "tied")
        score=3
    else:
        lose=1
        print(str(move) + "lost")
        score=0
    score = score + givescore(move[1])
    print(f"your score is {score}")
    totalscore=totalscore+score
print(f"your totalscore is {totalscore}")
print("the sample answer should be 15")