# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 18:43:28 2018

@author: 73251
"""

file=open('data.txt','r')
outfile=open('output.txt','w')
total=0
max_h=0
min_h=100
max_w=0
min_w=100
t_h=0
t_w=0
min_BMI=100
max_BMI=0
s_BMI=0
average_BMI=0
average_h=0
average_w=0


for line in file:
    line=line.strip()
    a=line.split()
    name=a[0]
    
    if total>0:
        h=float(a[1])
        w=float(a[2])
        BMI=w/h**2
        if BMI< min_BMI:
            min_BMI=BMI
        if BMI>max_BMI:
            max_BMI=BMI
        s_BMI=s_BMI+BMI
        average_BMI=s_BMI/8
    
        if h<min_h:
            min_h=h
        if h>max_h:
            max_h=h
        t_h+=h
        average_h=t_h/8
    
        if w<min_w:
            min_w=w
        if w>max_w:
            max_w=w
        t_w+=w
        average_w=t_w/8
        print(line,'{:10.2f}'.format(BMI))
    
    else:
        total+=1
        print(line,'BMI')
    


print('{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}'.format('\nAverage',average_h,average_w,average_BMI,'\nMax',max_h,max_w,max_BMI,'\nMin',min_h,min_w,min_BMI),file=outfile)
file.close()
outfile.close()

