# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 14:13:21 2018

@author: 73251
"""
    ###########################################################
    #  Computer Project #5
    #
    #  adoption of GM
    #    open the file
    #    read the file 
    #       set the max and min year
    #       compared with the data
    #       return the orgin
    #   main func to test the read def
    #       
    #    
    ###########################################################


STATES = ['Alaska', 'Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']


def open_file():#open the file
    print("Enter a file:")
    return open(input())

def read_file(file):
    file.readline()#read the file
    dictt = {}#def the dic as set

    for i in file.readlines(): 
        state = i.split(",")[0].strip()
        I=i.split(",")[6][:-1]
        y = int(i.split(",")[4])#year
        c = i.split(",")[1]#crop
        if I.isdigit():
            I=int(I)
        else:
            continue 
        if state == "Missouri 2/":#handle with the unknow reason
            state = "Missouri"
        if state not in STATES:#pass the others
            continue
        elif "All GE varieties" not in i.split(",")[3]:
            continue
        elif state not in STATES:
            continue
        data = {"Max Yr" : I,"Max" : I,"Min Yr" : y, "Min" : I}#set of data
        if c not in dictt:
            dictt[c] = {}#set a dictt when crop are not occur
        if state not in dictt[c].keys():
            dictt[c][state] = data
        else:
            if I > dictt[c][state]["Max"]:#point out max
                dictt[c][state]["Max Yr"] = y
                dictt[c][state]["Max"] = I
            if I < dictt[c][state]["Min"]:#point out min
                dictt[c][state]["Min Yr"] = y
                dictt[c][state]["Min"] = I
            if I == dictt[c][state]["Max"] and y < dictt[c][state]["Max Yr"]:
                dictt[c][state]["Max Yr"] = y
            if I == dictt[c][state]["Min"] and y < dictt[c][state]["Min Yr"]:
                dictt[c][state]["Min Yr"] = y
    return dictt

def main():#main function
    data = read_file(open_file())
    for c in sorted(data.keys()):
        print(" Crop: " +c)
        print("{:<20s}{:<8s}{:<6s}{:<8s}{:<6s}".format("State", "Max Yr", "Max", "Min Yr", "Min"))
        for states in sorted(data[c].keys()):
            print("{:<20s}{:<8s}{:<6d}{:<8s}{:<6d}".format(states, str(data[c][states]["Max Yr"]),data[c][states]["Max"],str(data[c][states]["Min Yr"]),data[c][states]["Min"]))

if __name__ == "__main__":
    main()