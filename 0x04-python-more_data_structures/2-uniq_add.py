#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = 0
    hashet = dict()  # creating an empty hashet.
    for i in range(len(my_list)):
        if (my_list[i] not in hashet.keys()):  # if it's not in the hashet,
            hashet[my_list[i]] = my_list[i]    # it'll be added.
            s += my_list[i]
    return(s)
