file=open("day1-input","r")

temp=file.readlines()

'''tl;dr 
out of groups of calories seperated by newlines which elf has the most?
5000
6000

7000
8000
9000'''


elfTotals=[]
tempTotal = 0
for calories in temp:
    if calories != "\n":
        tempTotal=tempTotal + int(calories)
    else:
        elfTotals.append(tempTotal)
        tempTotal=0
elfTotals.append(tempTotal)        
highest3=[0,0,0]

print(elfTotals.sort())
print(elfTotals)
highest3[1]=elfTotals[-1]
highest3[0]=elfTotals[-3]
highest3[2]=elfTotals[-2]
print(highest3)
print(f'the highest three are  {highest3[0]+highest3[1]+highest3[2]} ')
print("the sample answer should be 45000")