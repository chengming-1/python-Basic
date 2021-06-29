# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:56:35 2018

@author: 73251
"""

file=open('scores.txt')
form=[]
exam1=0
exam2=0
exam3=0
exam4=0
c_e1=0
c_e2=0
c_e3=0
c_e4=0

for line in file:
    name=line[:20]
    scores=line[20:]
    scores_p=scores.split()
    
    L_exam1=int(scores_p[0])
    exam1+=L_exam1
    c_e1+=1
    L_exam2=int(scores_p[1])
    exam2+=L_exam2
    c_e2+=1
    L_exam3=int(scores_p[2])
    exam3+=L_exam3
    c_e3+=1
    L_exam4=int(scores_p[3])
    exam4+=L_exam4
    c_e4+=1
    average=(L_exam1+L_exam2+L_exam3+L_exam4)/4
    
    form.append((name,L_exam1,L_exam2,L_exam3,L_exam4,average))
    
form.sort(key=lambda x:x[0])
print("{:20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10s}" .format('Name','Exam1','Exam2','Exam3','Exam4','Mean'))
for element in form:    
    print("{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}".format(element[0],element[1],element[2],element[3],element[4],element[5]))
print("{:20s}{:6.1f}{:6.1f}{:6.1f}{:6.1f}".format("Exam Mean",exam1/c_e1,exam2/c_e2,exam3/c_e3,exam4/c_e4))