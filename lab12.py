class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "("+str(self.x)+" "+str(self.y)+")"

    def __repr__(self):
        return "("+str(self.x)+" "+str(self.y)+")"

    def __add__(self,v):
        return Vector(self.x+v.x,self.y+v.y)

    def __sub__(self,v):
        return Vector(self.x-v.x,self.y-v.y)

    def __mul__(self,v):
        return Vector(self.x*v.x,self.y*v.y)
    
    def __rmul__(self,vector):
        return self.x*vector.x+self.y*vector.y


    def __eq__(self,vector):
        return self.x==vector.x and self.y==vector.y
    
    def magnitude(self):
        from math import sqrt
        return sqrt(self.x*self.x+self.y*self.y)
    
    def unit(self):
        import math
        dn = math.sqrt(self.x**2+self.y**2)
        if dn==0:
            raise ValueError()
        return Vector(self.x/dn,self.y/dn)