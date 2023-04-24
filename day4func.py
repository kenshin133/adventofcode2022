def extrapolateDash(dashSeperated):
    #print(dashSeperated)
    tempString=","
    for numf in range(int(dashSeperated.split('-')[0]),int(dashSeperated.split('-')[1])+1):
        #print(numf)
        tempString=tempString+str(numf)+","
    #print(tempString)    
    return tempString
