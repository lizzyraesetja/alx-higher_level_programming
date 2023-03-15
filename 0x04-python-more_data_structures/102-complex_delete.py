#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # if value in a_dictionary:
    #    del(a_dictionary[value])
    # return(a_dictionary)

    # for k, v in enumerate(a_dictionary):
    #    if v == value:
    #        del(a_dictionary[k])
    # return(a_dictionary)

    # a = {k:v for k, v in a_dictionary.items() if v != value}
    # return(a)

    pop_list = []
    for k, v in a_dictionary.items():
        if v == value:
            pop_list.append(k)
    for x in pop_list:
        a_dictionary.pop(x)
    return(a_dictionary)
