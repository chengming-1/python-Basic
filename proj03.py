    ###########################################################
    #  Computer Project #3
    #   calculate the GDP max/min change
    #   def function for open the file
    #   def function for min_percent
    #   def function for max_percent
    #   def function for calculate GDP and display the result
    #   main function:
    #       open file then do the calculations by sub-function
    ###########################################################
def open_file():#'''Repeatedly prompt until a valid file name allows the file to be opened.'''   
    Done = False
    while not Done:
        try:
            file=input("Enter a file name:")
            fp=open(file,"r") if file== "" else open(file)
            return fp
        except FileNotFoundError:
            print(" Error. Please try again")
            
    
def find_min_percent(line): #'''Find the min percent change in the line; return the value and the index.'''
    line_i=76  #the inital line required
    line_f=88   #the final line required
    index=0
    min_val=10**7
    min_val_index=-1
    for i in range(47):
        try:
            val=float(line[line_i:line_f].strip())
        except ValueError:
            continue
        if min_val > val:# decied which is min value in the data
            min_val = val
            min_val_index=i
        else:  
            pass
        line_i+=12
        line_f+=12
        index+=1
    return min_val,min_val_index

def find_max_percent(line): #'''Find the max percent change in the line; return the value and the index.'''
    line_i=76
    line_f=88
    max_val = 0
    max_val_index=-1
    for i in range(46):
        try:
            val=float(line[line_i:line_f].strip())
        except ValueError:
            continue
        if max_val < val:
            max_val = val
            max_val_index=i
        else:
            pass
        line_i+=12
        line_f+=12
    return max_val,max_val_index

def find_gdp(line, index):#'''Use the index fo find the gdp value in the line; return the value'''
    line_i=76
    line_f=88
    for i in range(49):
        if i ==index:
            return float(line[line_i:line_f].strip())#remove spaces
        else:
            pass
        line_i+=12
        line_f+=12

        
def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp): #'''Display values; convert billions to trillions first.'''   
    min_val_gdp=min_val_gdp/1000
    max_val_gdp=max_val_gdp/1000
    print('\nGross Domestic Product')
    print('{:<10s}{:>8s}{:>6s}{:>18s}'.format('min/max','change','year','GDP (trillions)'))
    print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format("min", min_val, min_year, min_val_gdp))
    print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format("max", max_val, max_year, max_val_gdp))

def main():                    
    main_file=open_file()
    line_number=0
    min_val=min_index=min_gdp=0
    max_val=max_index=max_gdp=0
    for line in main_file: # begin  read with the file
        if line_number == 8:# found the data of line 8
            max_val,max_index=find_max_percent(line)
            min_val,min_index=find_min_percent(line)
        elif line_number == 43:# found the data of line 43
            min_gdp=find_gdp(line,min_index)
            max_gdp=find_gdp(line,max_index)
        else:
            pass
        line_number+=1
    display(min_val, min_index + 1969, min_gdp, max_val, max_index + 1969, max_gdp )

# Calls the 'main' function only when you execute within Spyder (or console)
# Do not modify the next two lines.
if __name__ == "__main__":
    main()
    
