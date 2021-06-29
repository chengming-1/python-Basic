# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:55:34 2019

@author: 73251
"""

infile = open("data.txt", "r")
outfile = open("output.txt", "w")
infile.readline()
total=0
max_hei=0
min_hei=100
max_wei=0
min_wei=100
t_hei=0
t_wei=0
min_BMI=100
max_BMI=0
s_BMI=0
ave_BMI=0
ave_hei=0
ave_wei=0


for line in infile:
    line=line.strip()
    a=line.split()
    name=a[0]
    
    if total>0:
        hei=float(a[1])
        wei=float(a[2])
        BMI=wei/hei**2
        if BMI< min_BMI:
            min_BMI=BMI
        if BMI>max_BMI:
            max_BMI=BMI
        s_BMI=s_BMI+BMI
        ave_BMI=s_BMI/8
    
        if hei<min_hei:
            min_hei=hei
        if hei>max_hei:
            max_hei=hei
        t_hei+=hei
        ave_hei=t_hei/8
    
        if wei<min_wei:
            min_wei=wei
        if wei>max_wei:
            max_wei=wei
        t_wei+=wei
        ave_wei=t_wei/8
        print(line,'{:12.2f}'.format(BMI),file=outfile)
        
    
    else:
        total+=1
        print('Name     Height(m)      Weight(kg)     BMI',file=outfile)
print('{:<12s} {:<12.2f}{:<12.2f}{:<12.2f}{:<12s} {:<12.2f}{:<12.2f}{:<12.2f}{:<12s} {:<12.2f}{:<12.2f}{:<12.2f}'.format('\nAverage ',ave_hei,ave_wei,ave_BMI,'\nMax ',max_hei,max_wei,max_BMI,'\nMin ',min_hei,min_wei,min_BMI),file=outfile)

outfile.close()