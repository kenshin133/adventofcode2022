file=open("day7-input.sample","r")

temp=file.readlines()
from day7func import *

# '''How many characters need to be processed before the first start-of-packet marker which is 4 unique characters is detected?
#1


for sequence in temp:
    print(findstartofpacketp2(sequence))


print("answers for smaples should be : 95437")