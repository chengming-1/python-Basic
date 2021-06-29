# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 16:28:32 2018

@author: 73251
"""

lst={}
def open_file(lst):
    fp=open('data1.txt')
    for line in fp:
        (key,value)=line.split()
        if key=="Name" and value=="Score":
            continue
        if key in lst:
            lst[key]+=int(value)
        else:
            lst[key]=int(value)
            
    fp2=open('data2.txt')
    for line in fp2:
        (key,value)=line.split()
        if key=="Name" and value=="Score":
            continue
        if key in lst:
            lst[key]+=int(value)
        else:
            lst[key]=int(value)
            
def display_list(lst):
    print("{:10s} {:<10s}".format("Name","Total"))
    for key,val in sorted(lst.items()):
        print("{:10s} {:<10d}".format(key,val))
        
if __name__=="__main__":
    open_file(lst)
    display_list(lst)
    

          
