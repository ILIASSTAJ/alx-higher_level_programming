#!/usr/bin/python3
'''function that adds all unique integers in a list )'''


def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    result = 0

    for i in uniq_list:
        result += i
    return (result)
