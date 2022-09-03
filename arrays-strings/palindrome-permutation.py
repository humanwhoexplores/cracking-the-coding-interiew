"""
Given a String, Write a function to check if it is a permutation of a palindrome or not.

Assumption :- it is not case sensitive but contains only A-Z or a-z and whitespaces.
"""

# Checking if it is a permutation of palindrome or not
def checkPalindromePermutation(input_str):

    # Stripping extra space from each end
    input_str = input_str.lstrip()
    input_str = input_str.rstrip()
    
    # Converting everything into LowerCase 
    input_str = input_str.lower()

    hashMap = [0] * 128

    for c in input_str:
        hashMap[ord(c)] += 1
    
    odd_occurence = 0
    for i in range(96, len(hashMap)):
        if hashMap[i] %2 !=0:
            odd_occurence += 1
    
    if odd_occurence > 1:
        return False
    else:
        return True

if __name__ == '__main__':
    print(checkPalindromePermutation('Tact Coa'))
