file=open("day6-input.sample","r")

temp=file.readlines()
from day6func import *

# '''How many characters need to be processed before the first start-of-packet marker which is 4 unique characters is detected?
#1


for sequence in temp:
    print(findstartofpacket(sequence))


print("answers for smaples should be : \n     bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5 \n nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6 \n nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10 \n zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11")