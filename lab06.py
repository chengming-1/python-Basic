# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:01:22 2019

@author: 73251
"""

file=open('scores.txt')

exam1=0
exam2=0
exam3=0
exam4=0
count_ex1=0
count_ex2=0
count_ex3=0
count_ex4=0
format_s=[]

for line in file:
    name=line[:20]
    scores=line[20:]
    scores_p=scores.split()   
    line_exam1=int(scores_p[0])
    exam1+=line_exam1
    count_ex1+=1
    line_exam2=int(scores_p[1])
    exam2+=line_exam2
    count_ex2+=1
    line_exam3=int(scores_p[2])
    exam3+=line_exam3
    count_ex3+=1
    line_exam4=int(scores_p[3])
    exam4+=line_exam4
    count_ex4+=1
    average=(line_exam1+line_exam2+line_exam3+line_exam4)/4   
    format_s.append((name,line_exam1,line_exam2,line_exam3,line_exam4,average))    
format_s.sort(key=lambda x:x[0])
print("{:20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10s}" .format('Name','Exam1','Exam2','Exam3','Exam4','Mean'))
for line in format_s:    
    print("{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}".format(line[0],line[1],line[2],line[3],line[4],line[5]))
print("{:20s}{:6.1f}{:6.1f}{:6.1f}{:6.1f}".format("Exam Mean",exam1/count_ex1,exam2/count_ex2,exam3/count_ex3,exam4/count_ex4))