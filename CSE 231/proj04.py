
    ###########################################################
    #  Computer Project #4
    #
    #  def open_file to load the data
    #       read the file by read_file
    #       def find_average and Median to caculate the number from list
    #       def get range and percent to caculate the value 
    #   main def to loop the funtion below
    #       if to ensure the year with string'Yes'
    #   input the choice 
    #       while ensure the choice and split r and p
    #   elif to make the income 
    #   display result    
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
    while True:#true to start loop
        year_str = input("Enter a year where 1990 <= year <= 2015: ")
        try:#make sure the year is in the range
            if not (int(year_str) <= 2015 and int(year_str) >= 1990): 
                raise ValueError
        except ValueError:
            print("Error in year. Please try again.")
            continue
        try:#make sure the file is in the true data
            f=open("year" + year_str + ".txt")
            return f
        except FileNotFoundError:
            print('Error in file name: {}  Please try again.'.format("year" + year_str + ".txt"))
            continue
        
def read_file(fp):#for read the file
    line=list(fp.readlines())#list the data
    return line[2:]
        
def find_average(data_lst):# find the average  in data
    NOP=int(str(data_lst[-1].split()[4]).replace(",",""))#save number
    sum=0.0
    for s in data_lst:
        lst=s.split()
        sum=float(lst[6].replace(",", ""))+sum
    return sum/NOP#average

def find_median(data_lst):#find the median in data
    median=100
    AI=0
    for s in data_lst:
        lst=s.split()
        if abs(float(lst[5])-50) < median:
            median=abs(float(lst[5])-50)#median
            AI=float(lst[7].replace(",", ""))
    return AI
    
def get_range(data_lst, percent):
    for s in data_lst:
        lst=s.split()
        if float(lst[5]) >= percent:
            return (float(lst[0].replace(",", "")), float(lst[2].replace(",", ""))), float(lst[5]), float(lst[7].replace(",", ""))
            #range

def get_percent(data_lst,salary):
    for s in data_lst[:-1]:
        lst=s.split()
        if salary < float(lst[2].replace(",", "")) and salary >= float(lst[0].replace(",", "")):
            return (float(lst[0].replace(",", "")), float(lst[2].replace(",", ""))), float(lst[5])
    return (float(lst[0].replace(",", "")), float("inf")), float(lst[5])#percent

def main():#def the main function and adds funtion for calculation
    f=open_file()
    List=read_file(f)
    year=int(f.name[4:8])
    average=find_average(List)
    median=find_median(List)
    print("{:<6s}{:<14s}{:<14s}".format('Year','Mean','Median'))
    print("{:<6d}${:<14,.2f}${:<14,.2f}".format(year,average,median))#get the data from given 
    response = input("Do you want to plot values (yes/no)? ")
    if response.lower() == 'yes':
        a=list()#for list in 0-40 and get the position of six
        b=list()#delete the semic 
        for s in List[:40]:
            lst=a.split()
            a.append(float(lst[5]))
            b.append(float(lst[0].replace(",", ""))) 
    choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
    while choice:
        if choice=='r':#check for range
            P=float(input('Enter a percent: '))
            if P<=100 and P>=0:#make sure percent are in 0-1
                print("{:4.2f}% of incomes are below ${:<13,.2f}.".format(P, get_range(List, P)[0][0]))
            else:
                print("Error in percent. Please try again")
        elif choice == 'p':#check for percent
            IC = float(input("Enter an income: "))
            if IC >= 0:#make sure income are bigger than zero
                print("An income of ${:<13,.2f} is in the top {:4.2f}% of incomes.".format(IC, get_percent(List, IC)[1]))
            else:
                print("Error: income must be positive")
        elif choice == '\n':
            break
        else:
            print('Error in selection.')
        choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
if __name__ == "__main__":
    main()