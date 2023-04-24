def extrapolateDash(dashSeperated):
    #print(dashSeperated)
    tempString=","
    for numf in range(int(dashSeperated.split('-')[0]),int(dashSeperated.split('-')[1])+1):
        #print(numf)
        tempString=tempString+str(numf)+","
    #print(tempString)    
    return tempString

def extrapolateDashArray(dashSeperated):
    #print(dashSeperated)
    templist=[]
    for numf in range(int(dashSeperated.split('-')[0]),int(dashSeperated.split('-')[1])+1):
        #print(numf)
        templist.append(numf)
    print(templist)
    return templist

def FindCommoninArray(list1,list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
            else:
                pass