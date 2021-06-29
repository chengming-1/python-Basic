# -*- coding: utf-8 -*-
"""
Created on Wed May 29 13:46:09 2019

@author: 73251
"""

def leap_year(year):
    year=int(year)
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year %100 != 0 and year % 4 == 0:
        return True
    else:
        return False

def rotate(s,n):
    if s.strip():
        x=s[-n:]
        y=s[:-n]
        return x + y
    else:
        return s

def digit_count(number):
    if float(number) < 1.0:
        return (0,0,1)
    even_count=0
    odd_count=0
    zero_count=0   
    num=str(number)
    length=0
    while length<len(num):
        if num[length] == '.':
            break        
        value = int(num[length])
        if value == 0:
            zero_count += 1
        elif value % 2 == 1:
            odd_count += 1
        elif value % 2== 0 and value !=0:
            even_count += 1 
        length +=1
    return(even_count,odd_count,zero_count)
    


def float_check(number):
    if number.count('.') > 1:
        return False
    elif number.count('e') > 0:
        return False
    else:
        try:
            float(number)
            return True
        except:
            return False
        
