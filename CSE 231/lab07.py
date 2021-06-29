# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 14:10:34 2018

@author: 73251
"""
file=input('Enter a file name:')
fp=open(file)
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
c7=0
c8=0
c9=0
number_list=[c1,c2,c3,c4,c5,c6,c7,c8,c9]
for n,line in enumerate(fp):
    line=line.strip()
    if line[0].isdigit():
        if line[0]=='1':
            number_list[0]+=1
        elif line[0]=='2':
            number_list[1]+=1
        elif line[0]=='3':
            number_list[2]+=1
        elif line[0]=='4':
            number_list[3]+=1
        elif line[0]=='5':
            number_list[4]+=1
        elif line[0]=='6':
            number_list[5]+=1
        elif line[0]=='7':
            number_list[6]+=1
        elif line[0]=='8':
            number_list[7]+=1
        elif line[0]=='9':
            number_list[8]+=1
    else:
        pass
    
count=sum(number_list)
a=(number_list[0]*100)/count
b=(number_list[1]*100)/count
c=(number_list[2]*100)/count
d=(number_list[3]*100)/count
e=(number_list[4]*100)/count
f=(number_list[5]*100)/count
g=(number_list[6]*100)/count
h=(number_list[7]*100)/count
i=(number_list[8]*100)/count

print()
print('{:6s}{:>8s} {:8s}'.format("Digit","Percent","Benford"))
print('{:>6s}{:>7.1f}% {:<8s}'.format('1:',a,'(30.1%)'))
print('{:>6s}{:>7.1f}% {:<8s}'.format('2:',b,'(17.6%)'))
print('{:>6s}{:>7.1f}% {:<8s}'.format('3:',c,'(12.5%)'))
print('{:>6s}{:>7.1f}% {:<8s}'.format('4:',d,'( 9.7%)'))
print('{:>6s}{:>7.1f}% {:<8s}'.format('5:',e,'( 7.9%)'))
print('{:>6s}{:>7.1f}% {:<8s}'.format('6:',f,'( 6.7%)'))
print('{:>6s}{:>7.1f}% {:<8s}'.format('7:',g,'( 5.8%)'))
print('{:>6s}{:>7.1f}% {:<8s}'.format('8:',h,'( 5.1%)'))
print('{:>6s}{:>7.1f}% {:<8s}'.format('9:',i,'( 4.6%)'))