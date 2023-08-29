#!/usr/bin/python3
'''function that returns the number of keys in a dictionary'''


def number_keys(a_dictionary):
    num1 = 0
    list_keys = list(a_dictionary.keys())

    for i in a_dictionary.keys():
        num1 += 1
    print(list_keys)
    return (num1)
