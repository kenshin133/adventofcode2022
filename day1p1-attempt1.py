file=open("day1-input","r")

temp=file.readlines()

# '''tl;dr 
# out of groups of calories seperated by newlines which elf has the most?
# 5000
# 6000

# 7000
# 8000
# 9000'''


elfTotals=[]
tempTotal = 0
for calories in temp:
    if calories != "\n":
        tempTotal=tempTotal + int(calories)
    else:
        elfTotals.append(tempTotal)
        tempTotal=0
highest=0
for calories in elfTotals:
    if calories > highest:
        highest = calories
    else:
        pass
print(f'the highest is {highest}')
print("the sample answer should be 24000")