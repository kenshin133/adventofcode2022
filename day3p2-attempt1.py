file=open("day3-input","r")

temp=file.readlines()
from day3func import *
# '''tl;dr
#    So, in the above example, the first group's rucksacks are the first three lines:

# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# And the second group's rucksacks are the next three lines:

# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw
# In the first group, the only item type that appears in all three rucksacks is lowercase r; this must be their badges. In the second group, their badge item type must be Z.

# Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (r) for the first group and 52 (Z) for the second group. The sum of these is 70.

# Find the item type that corresponds to the badges of each three-Elf group.'''
newgroup=GroupMultiple(temp, 3)
totalitems=0
for elf in newgroup:
    common=find3Common(elf[1], elf[0], elf[2])
    prio=findPriority(common)
    totalitems=totalitems+prio

    print(common)
    print(totalitems)
print("the total for sample should be 70")