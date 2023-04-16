def splitInput(input):
    compartments=[]
    compartments.append(input[0:len(input)//2])
    compartments.append(input[len(input)//2:])
    return compartments

def findCommon(side1,side2):
    for _ in side1:
        if _ in side2:
            print(_)
            return _