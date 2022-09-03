"""
    There are 3 Types of Edits that can be performed on a string :- Insert a Character, 
    Remove a Character, Replace a Character.
    Given 2 String, Write some code to check if they are one edit away or not.

    Assuming we have small letters only in the strings
"""

def checkOneEditAway(input_str1, input_str2):
    # checking if they are one edit away or not
    
    # 0 Edits Away
    if input_str1 == input_str2:
        return True
    
    hashMap1 = [0] * 26
    hashMap2 = [0] * 26 

    # 1 edit away
    for c in input_str1:
        hashMap1[ord(c) - 97] += 1

    for c in input_str2:
        hashMap2[ord(c) - 97] += 1   
    
    diff = 0 
    for i in range(0, len(hashMap1)):
        if hashMap1[i] != hashMap2[i]:
            diff += 1
    
    if diff > 2:
        return False
    else: 
        return True
    
if __name__ == '__main__':
    print(checkOneEditAway('pale', 'ple'))
    print(checkOneEditAway('pales', 'pale'))    
    print(checkOneEditAway('pale', 'bale'))
    print(checkOneEditAway('pale', 'bake'))