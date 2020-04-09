# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def unique(list):
    unique_list=[]
    for x in list:
        if x not in unique_list:
            unique_list.append(x)
        else:
            pass
    print(unique_list)
unique({1,2,3,4,3,7,1,1,2,3,1,3})



    
    
