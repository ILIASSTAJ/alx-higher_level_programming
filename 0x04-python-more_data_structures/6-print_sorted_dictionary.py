#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    #for k in list_ord:
        #print("{}: {}".format(k, a_dictionary.get(k)))
    for i in sorted(a_dictionary):
        print("{}: {}".format(i, a_dictionary.get(i)))
    print(a_dictionary)
    print(list_ord)


