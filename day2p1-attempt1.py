file=open("day2-input.sample","r")

temp=file.readlines()

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
'''For example, suppose you were given the following strategy guide:

A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?'''

moves=[]
score=0
#get rid of newlines, turn into list of lists.
for i in range(0,len(temp)):
    moves.append(temp[i].replace('\n', '').split(' '))

for move in moves:
    won=0
    tie=0
    lose=0
    if iswin(move):
        won=1
        print(str(move) + "won")
    elif istie(move):
        tie=1
        print(str(move) + "tied")
    else:
        lose=1
        print(str(move) + "lost")


print("the sample answer should be 15")