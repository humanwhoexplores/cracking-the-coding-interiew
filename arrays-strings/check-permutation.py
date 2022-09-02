"""
    Given 2 Strings, Write a Program to check if both strings are permutation of each other
    
    There are 2 solutions 
    + Sort the Strings and compare 
    + check if character count of various characters in each string is same or not

    Considerations :- It is sensitive to Case and Space
"""

def checkPermutationSorting(input_str1, input_str2):
    # sorting the strings

    input_str1 = ''.join(sorted(input_str1))
    input_str2 = ''.join(sorted(input_str2))

    if input_str1 == input_str2:
        return True 
    else:
        return False
 

def checkPermutationHashMap(input_str1, input_str2):
    # checking if it is a permutation of HashMap or not 
    hashMap1 = [0] * 128
    hashMap2 = [0] * 128
    
    for c in input_str1:
        hashMap1[ord(c)] += 1
        
    for c in input_str2:
        hashMap2[ord(c)] += 1
        
    if hashMap1 == hashMap2:
        return True
    else: 
        return False

   

if __name__ == '__main__':
    print(checkPermutationSorting("god", "dog"))
    print(checkPermutationSorting("god", "dog "))

    print(checkPermutationHashMap("god", "dog"))
    print(checkPermutationHashMap("god", "dog "))
    



