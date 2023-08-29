#!/usr/bin/python3
''' function that returns a set of common elements in two sets.'''


def common_elements(set_1, set_2):
    nset_1 = set(set_1)
    nset_2 = set(set_2)
    return (nset_1 & nset_2)
