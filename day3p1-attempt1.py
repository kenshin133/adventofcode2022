file=open("day3-input","r")

temp=file.readlines()
from day3func import *
# '''tl;dr
#     For example, suppose you have the following list of contents from six rucksacks:

#     vJrwpWtwJgWrhcsFMMfFFhFp
#     jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
#     PmmdzqPrVvPwwTWBwg
#     wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
#     ttgJtRGJQctTZtZT
#     CrZsJsPPZsGzwwsLwLmpwMDw
#     The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
#     The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
#     The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
#     The fourth rucksack's compartments only share item type v.
#     The fifth rucksack's compartments only share item type t.
#     The sixth rucksack's compartments only share item type s.
#     To help prioritize item rearrangement, every item type can be converted to a priority:

#     Lowercase item types a through z have priorities 1 through 26.
#     Uppercase item types A through Z have priorities 27 through 52.
#     In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

#     Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
# '''
rucksacks=[]
for rucksack in temp:
    rucksacks.append(splitInput(rucksack.replace('\n','')))
print(rucksacks)
totalitems=0
for sack in rucksacks:
    common=findCommon(sack[0],sack[1])
    prio=findPriority(common)
    print(sack[0],sack[1])
    print(prio)
    totalitems=totalitems+prio
    print(totalitems)
print("the total for sample should be 157")