def findstartofpacket(packet):
    buffer=[]
    position=0
    for bit in packet:
        #set first 4 bits
        if len(buffer) < 4:
            buffer.append(bit)
        else:
            if checkUnique(buffer):
                return buffer,position
            else:
                #advance the buffer
                buffer.append(bit)
                buffer.pop(0)
        position=position+1

def checkUnique(list):
    unique=0
    for letter in list:
        if unique != 3:
            if list.count(letter) != 1:
                return False
            else:
                unique=unique+1 
        else:
            return True

def findstartofpacketp2(packet):
    buffer=[]
    position=0
    for bit in packet:
        #set first 4 bits
        if len(buffer) < 14:
            buffer.append(bit)
        else:
            if checkUniquep2(buffer):
                return buffer,position
            else:
                #advance the buffer
                buffer.append(bit)
                buffer.pop(0)
        position=position+1

def checkUniquep2(list):
    unique=0
    for letter in list:
        if unique != 13:
            if list.count(letter) != 1:
                return False
            else:
                unique=unique+1 
        else:
            return True
#TODO: get first 4 items
#TODO: check if unique
#append/pop to get new listing
#TODO: recheck and return index.
#list.append to add to end
#list.pop(0) will remove the first item, list.pop() removes the last        
#DO: get first 4 items
#TODO: check if unique
#append/pop to get new listing
#TODO: recheck and return index.
#list.append to add to end
#list.pop(0) will remove the first item, list.pop() removes the last