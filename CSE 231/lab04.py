# -*- coding: utf-8 -*-
"""
Created on Wed May 30 14:03:34 2018

@author: 73251
"""
def leap_year(y):
    y=int(eval(y))
    if y%100==0 and y%400==0:
        return True
    elif y%100!=0 and y%4==0:
        return True
    else:
        return False




def rotate(s,n):
    if s.strip():
        a=s[-n:]
        h=s[:-n]
        return a+h
    else:
        return s

def digit_count(number):
    even=0
    odd=0
    zero=0
    number=str(number)
    number=number.split('.')[0]
    if(number=='0'):
        pass
    else:
        for each in number:
            value=int(each)
            if value%2==0 and value!=0:
                even+=1
            if value%2>0:
                odd+=1
            if value==0:
                zero+=1
    return(even,odd,zero)




def float_check(num):
    if num.count('.')>1:
        return False
    elif num.count('e')>0:
        return False
    else:
        try:
            float(num)
            return True
        except:
            return False
        
