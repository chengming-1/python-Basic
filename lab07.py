import csv
from operator import itemgetter

industry = ['Agriculture', 'Business services', 'Construction', 'Leisure/hospitality', 'Manufacturing']

def read_file(fp):
    data = []
    r_fp = csv.reader(fp)
    for i,index in enumerate(r_fp):
        if i <= 3 or i ==5 or i >= 57:
            pass
        else:
            data.append(index)
    return data

def get_totals(L):    
    states = 0
    for i in L[1:]:
        total = int("".join(L[0][1]))
        total = total.split(",")
        num = "".join(i[1])
        num = num.split(",")
        if num.isnumber():
            states += int(num)
        else:
            states = states + int(num[1:])
    return total, states

def get_industry_counts(L):
    count = {}
    List = []
    for i in L[1:]:
        if i[9] in industry:
            if i[9] not in count:
                count[i[9]] = 1
            else:
                count[i[9]] = count[i[9]] + 1  
    for i, index in count.items():
        List.append([i, index])
    List.sort(key = itemgetter(1),reverse = True )
    return List

def get_largest_states(L):
    part_percent = []
    total_percent = L[0][2]
    for i in L[1:]:
        if i[2] > total_percent:
            part_percent.append(i[0])
    return part_percent


def main():    
    fp = open("immigration.csv")
    L = read_file(fp)
    
    us_pop,total_pop = get_totals(L)
    if us_pop and total_pop:  # if their values are not None
        print("\nData on Illegal Immigration\n")
        print("Summative:", us_pop)
        print("Total    :", total_pop)
    
    states = get_largest_states(L)
    if states:  # if their value is not None
        print("\nStates with large immigrant populations")
        for state in states:
            state = state.replace('\n',' ')
            print(state)        
    
    counters = get_industry_counts(L)
    if counters:  # if their value is not None
        print("\nIndustries with largest immigrant populations by state")
        print("{:24s} {:10s}".format("industry","count"))
        for tup in counters:
            print("{:24s} {:2d}".format(tup[0],tup[1]))
        
if __name__ == "__main__":
    main()
