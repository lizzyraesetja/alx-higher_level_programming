#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return(0)
    s = 0
    d = 0
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            s = s + (my_list[i][j] * my_list[i][j+1])
            d = d + my_list[i][j+1]
            break
    return(s / d)
