file=open("day4-input","r")

temp=file.readlines()
from day4func import *

elfpairs=[]
#prep the array to be used
for i in temp:
    elfpairs.append(i.replace('\n','').split(","))


print(elfpairs)
totalpairs=0
for pair in elfpairs:
    if extrapolateDash(pair[0]) in extrapolateDash(pair[1]) or extrapolateDash(pair[1]) in extrapolateDash(pair[0]):
        print(f'found one, {extrapolateDash(pair[0])} and {extrapolateDash(pair[1])}')
        print(f'found one, {pair[0]} and {pair[1]}')
        totalpairs = totalpairs + 1
print(f'we found {totalpairs} total pairs')
print("the answer should be 2")
