
    ###########################################################
    #  Computer Project #5
    #  make the set of states which need to list in display
    #   open file
    #   read file
    #       make a dictionary as year and crop
    #       find the min and max and remove error
    #       return the data to dict for function to display
    #   display the result from the data given above
    ###########################################################
    
STATES = ['Alaska', 'Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']


def open_file():#open the file
    print("Enter a file:")
    fp = open(input())
    return fp

def read_file(file):
    file.readline()#read the file
    Dict = {}#the set 

    for i in file.readlines(): 
        Maxyr=i.split(",")[6][:-1]#max year(be pending)
        Minyr = int(i.split(",")[4])#min year(be pending)
        state = i.split(",")[0].strip() #state
        crop = i.split(",")[1]#crop
        if Maxyr.isdigit():
            Maxyr=int(Maxyr)
        else:
            continue 
        
        if state == "Missouri 2/":#make the error 2/ to be correct
            state = "Missouri"        
        if "All GE varieties" not in i.split(",")[3]:
            continue
        elif state not in STATES:
            continue

        data = {"Max Yr" : Maxyr,"Max" : Maxyr,"Min Yr" : Minyr, "Min" : Maxyr}#the set of max year and min year
        
        if crop not in Dict:
            Dict[crop] = {}#set a dictionary if crop are not occuring
        if state not in Dict[crop].keys():
            Dict[crop][state] = data
        else:
            if Maxyr < Dict[crop][state]["Min"]:
                Dict[crop][state]["Min Yr"] = Minyr #ensure the min year if current value are not smallest
                Dict[crop][state]["Min"] = Maxyr
            if Maxyr > Dict[crop][state]["Max"]:
                Dict[crop][state]["Max Yr"] = Minyr
                Dict[crop][state]["Max"] = Maxyr#ensure the max year if current value are not biggest
            if Maxyr == Dict[crop][state]["Min"] and Minyr < Dict[crop][state]["Min Yr"]:
                Dict[crop][state]["Min Yr"] = Minyr
            if Maxyr == Dict[crop][state]["Max"] and Minyr < Dict[crop][state]["Max Yr"]:
                Dict[crop][state]["Max Yr"] = Minyr
    return Dict #return the value list as Dict

def main():#main function
    data = read_file(open_file())
    for crop in sorted(data.keys()):
        print(" Crop: " +crop)
        print("{:<20s}{:<8s}{:<6s}{:<8s}{:<6s}".format("State", "Max Yr", "Max", "Min Yr", "Min"))
        for states in sorted(data[crop].keys()):
            print("{:<20s}{:<8s}{:<6d}{:<8s}{:<6d}".format(states, str(data[crop][states]["Max Yr"]),data[crop][states]["Max"],str(data[crop][states]["Min Yr"]),data[crop][states]["Min"]))

if __name__ == "__main__":
    main()