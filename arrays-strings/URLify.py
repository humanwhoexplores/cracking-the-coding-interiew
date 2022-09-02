"""
    Write a Program to replace all spaces in a string with %20
"""

def urlify(input_str):

    input_str = input_str.rstrip()

    char_list = []

    for c in input_str:
        char_list.append(c)
    
    for i in range(len(char_list)):
        if char_list[i] == ' ':
            char_list[i] = '%20'

    output_str = str()   
    for c in char_list:
        output_str += c
    
    return output_str

if __name__ == '__main__':
    print(urlify("Mr John Smith "))

