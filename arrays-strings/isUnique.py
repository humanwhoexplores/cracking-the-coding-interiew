""""
    Let's Crunch Dude: Problem IsUnique
    Implement an algorithm to determine if a string has all unique characters.
    Additonal :- what if we cannot use additional space ? 

    Things to ask :- 
    is it an ASCII String or UniCode String 
    For Simplicity let's consider it is a ASCII String
    numer of AScii characters = 128 
    number of UNICODE Characters = 144697
"""

def isUniquechars(input_str):

    #  if the length of string is > 128 : then it is bound to have repeats : isn't it ? 
    if len(input_str) > 128:
        return False
    
    # Creating a HashMap of Various Characters 
    hashMap = [False] * 128

    for c in input_str:
        if hashMap[ord(c)] == True:
            return False
        else:
            hashMap[ord(c)] = True

    return True


if __name__ == '__main__':
    ret_value = isUniquechars("123qwerq")
    print("return value is ", ret_value)

