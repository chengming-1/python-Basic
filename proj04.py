    ###########################################################
    #  Computer Project #4
    #
    #  AWI of the one percent
    #   import pylab
    #   open the file with true years which included in the data base
    #   to find the average
    #   find the median
    #   get the range
    #   calculate the percent
    #   main to display
    #   
    ###########################################################
import pylab

def do_plot(x_vals,y_vals,year):
    '''Plot x_vals vs. y_vals where each is a list of numbers of the same length.'''
    pylab.xlabel('Income')
    pylab.ylabel('Cumulative Percent')
    pylab.title("Cumulative Percent for Income in "+str(year))
    pylab.plot(x_vals,y_vals)
    pylab.show()
    
def open_file():
    while True:#start loop
        year_str = input("Enter a year where 1990 <= year <= 2015: ")
        try:
            if not (int(year_str) >= 1990 and int(year_str) <= 2015): # make sure the year  in the range correctly
                raise ValueError
        except ValueError:
            print("Error in year. Please try again.")
            continue
        try:                                       #make sure the file correctly
            fp=open("year" + year_str + ".txt")
            return fp
        except FileNotFoundError:
            print('Error in file name: {}  Please try again.'.format("year" + year_str + ".txt"))
            continue
        
def read_file(fp):
    line=list(fp.readlines())    #list the data from file
    return line[2:]
        
def find_average(data_lst):
    total=0.0
    times=int(str(data_lst[-1].split()[4]).replace(",","")) #make str to int without space and comma
    for number in data_lst:
        lst=number.split()
        total += float(lst[6].replace(",", ""))
    return total/times # calculate average
    
def find_median(data_lst):
    median = 0
    conf = 100
    for number in data_lst:
        lst = number.split()
        if abs(float(lst[5])-50) < conf: # compared with two value to ensure the median
            conf=abs(float(lst[5])-50.0)
            median=float(lst[7].replace(",", ""))
    return median
        
def get_range(data_lst, percent):
    for number in data_lst:
        List=number.split()
        if float(List[5]) >= percent: # for the range 
            a=float(List[0].replace(",", "")), float(List[2].replace(",", ""))
            b=float(List[5])
            c=float(List[7].replace(",", ""))
            return a,b,c # return the number required

def get_percent(data_lst,salary):
    for number in data_lst[:-1]:
        lst=number.split()
        if salary < float(lst[2].replace(",", "")) and salary >= float(lst[0].replace(",", "")):
            a=float(lst[0].replace(",", ""))#columus 0
            b=float(lst[2].replace(",", ""))#columus 2
            c=float(lst[5])
            return (a,b),c       
    return (a, float("inf")), c#percent

    
    
def main():#def the main function and adds funtion for calculation
    fp=open_file()
    lst=read_file(fp)
    year=int(fp.name[4:8])
    median=find_median(lst)
    average=find_average(lst)
    print("{:<6s}{:<14s}{:<14s}".format('Year','Mean','Median'))
    print("{:<6d}${:<14,.2f}${:<14,.2f}".format(year,average,median))#get the data from given 
    response = input("Do you want to plot values (yes/no)? ")
    if response.lower() == 'yes':
        lst1=list()#for list in 0-40 and get for 6
        lst2=list()#delete comma and add to the first number
        for number in lst[:40]:
            lst=lst1.split()
            lst1.append(float(lst[5]))
            lst2.append(float(lst[0].replace(",", ""))) 
    choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
    while choice:
        if choice=='r':#check for range
            percent=float(input('Enter a percent: '))
            if percent<=100 and percent>=0:# percent are in 0% to 100% correctly
                print("{:4.2f}% of incomes are below ${:<13,.2f}.".format(percent, get_range(lst, percent)[0][0]))
            else:
                print("Error in percent. Please try again")
        elif choice == 'p':#check for percent
            icn = float(input("Enter an income: "))
            if icn < 0:#make sure income are bigger than zero
                print("Error: income must be positive")
            else:
                print("An income of ${:<13,.2f} is in the top {:4.2f}% of incomes.".format(icn, get_percent(lst, icn)[1]))
        elif choice == '\n':
            break
        else:
            print('Error in selection.')
        choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
if __name__ == "__main__":
    main()