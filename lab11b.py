# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 14:53:00 2019

@author: 73251
"""

class Time(object):
   def __init__(self,h=0,m=0,s=0):
       self.__h=h
       self.__m=m
       self.__s=s
  
   def __repr__(self):
       output = "Class Time: {:02d}:{:02d}:{:02d}".format(self.__h,self.__m,self.__s)
       return output
  
   def __str__(self):
       output = "{:02d}:{:02d}:{:02d}".format(self.__h,self.__m,self.__s)
       return output
   
   def display(self,time):
       Time= time.split(':')
       self.__h=int(Time[0])
       self.__m=int(Time[1])
       self.__s=int(Time[2])
       
A = Time(12,25,30)
print(A)
print(repr(A))
print(str(A))
print()

B = Time(2,25,3)
print(B)
print(repr(B))
print(str(B))
print()

C = Time(2,25)
print(C)
print(repr(C))
print(str(C))
print()

D = Time()
print(D)
print(repr(D))
print(str(D))
print()
D.display( "03:09:19" )
print(D)
print( repr( D ) )
print( str( D ) )   