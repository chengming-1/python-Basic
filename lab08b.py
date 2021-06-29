# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 14:20:15 2019

@author: 73251
"""

List={}
def open_file(List):
    fp=open('data1.txt')
    for line in fp:
        (i,value)=line.split()
        if i=="Name" and value=="Score":
            continue
        if i in List:
            List[i]+=int(value)
        else:
            List[i]=int(value)
            
    fp2=open('data2.txt')
    for line in fp2:
        (i,value)=line.split()
        if i=="Name" and value=="Score":
            continue
        if i in List:
            List[i]+=int(value)
        else:
            List[i]=int(value)
            
def display_list(List):
    print("{:10s} {:<10s}".format("Name","Total"))
    for key,val in sorted(List.items()):
        print("{:10s} {:<10d}".format(key,val))
        
if __name__=="__main__":
    open_file(List)
    display_list(List)