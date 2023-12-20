'''
Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
'''

def string(test_str):
    word_list=test_str.split("-")
    sorted_list=sorted(word_list)
    return("-".join(sorted_list))



print(string("green-red-yellow-black-white"))