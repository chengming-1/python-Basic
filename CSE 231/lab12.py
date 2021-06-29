# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 22:07:25 2018

@author: 73251
"""
import math
class Vector(object):
    def __init__(self,x=0,y=0):
        self1=x
        self2=y
    def __str__(self):
        return "(%f,%f)"%(self1,self.y)
    def __repr__(self, **kwargs):
        return "Vector(%f,%f)"%(self1,self.y)
    def __add__(self,vector):
        v=Vector(self.x+vector.x,self.y+vector.y)
        return v
    def __sub__(self,vector):
        v=Vector(self.x-vector.x,self.y-vector.y)
        return v
    def __mul__(self,vector):
        return self.x*vector.x+self.y*vector.y
    def __eq__(self,vector):
        if(self.x==vector.x and self.y==vector.y):
            return True
        return False   
    def magnitude(self):
        return math.sqrt(self.x**2+self.y**2)
    def unit(self):
        try:
            if(self.magnitude()==0):
                raise ValueError
            else:
                1/self.magnitude()
        except ValueError:
            print("cannot convert zero vector to unit vector")