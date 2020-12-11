def reverse(String):
    return String[::-1]


def circularString(refString, length, startIndex, moveNumb):
    string = refString[startIndex-1:startIndex-1+length+1]
    if moveNumb > 0:
        string = refString[startIndex+abs(moveNumb)-1:startIndex+abs(moveNumb)+length-1]
        return string
    elif moveNumb == 0:
        return string
    else:
        temp = refString[len(refString)+moveNumb:]
        temp += string[:len(string)-moveNumb]
        return temp
