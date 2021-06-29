# -*- coding: utf-8 -*-
"""
Created on Tue May 29 15:43:19 2018

@author: 73251
"""
print("Welcome to change-making program.")
val= input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")
numVal= float(val)
total=410
change=0
x=0
y=0
z=0
m=0
save=0
t=0
quarters = 10
dimes = 10
pennies = 10
nickels = 10
paying=True
end=False

while not (val=="q")and not end:
    numVal= float(val)
    paying=True
    if (numVal<0):
        print("\nError: purchase price must be non-negative.")

    else:
        while paying:
            paid=float(input("\nInput dollars paid (int): "))
            print()
            if(paid>=numVal):
                change=paid-numVal
                t=change
                change*=100
                save=change

                if(change<=total):
                    total-=change
                    if(quarters>0):
                        x=int(change//25)
                        quarters-=x
                        if(quarters<0):
                            change%=25
                            change-=quarters*25
                            x+=quarters
                            quarters-=quarters
                        else:
                            change%=25

                    if(dimes>0):
                        y=int(change//10)
                        dimes-=y
                        if(dimes<0):
                            change%=10
                            change-=dimes*10
                            y+=dimes
                            dimes-=dimes

                        else:
                            change%=10
                    if(pennies>0): 
                        z=int(change//5)
                        pennies-=z
                        if(pennies<0):
                            change%=5
                            change-=pennies*5
                            z+=pennies
                            pennies-=pennies
                        else:
                            change%=5
                
                    if(nickels>0):  
                        change=int(round(change, 1))
                        m=int(change//1)
                        pennies-=m
                        if(nickels<0):
                            change%=1
                            change-=nickels
                            m+=nickels
                            nickels-=nickels
                        else:
                            change%=1
                        
                    if(save==0):
                        print("\nNo change")
                        
                    else:
                        print("Collect change below: ")
                        if(x>0):
                            print("Quarters:",x,)
                        if(y>0):
                            print("Dimes:",y,)
                        if(z>0):
                            print("Nickels:",z,)
                        if(m>0):
                            print("Pennies:",m,)
                    print("Stock:",quarters,"quarters,",dimes,"dimes,",nickels,"nickels, and",pennies,"pennies")

                else:
                    print("\nError: ran out of coins.")
                    end=True
                paying=False

            else:
                print("\nError: insufficient payment.")

    if not end:
        val= input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")
