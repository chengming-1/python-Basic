def open_file():
    find = True
    while find:
        try:
            file=input("Enter a file name:")
            fp=open("GDP.txt")
            return fp
        except IOError:
            print("Error. please try again")
            
def find_min_percent(line):
    x=76
    y=88
    index=0
    min_value=10**7
    min_value_index=-1
    for i in range(47):
        try:
            value=float(line[x:y].strip())
        except ValueError:
            continue
        if min_value > value:
            min_value = value
            min_value_index=i
        else:
            pass
        x+=12
        y+=12
        index+=1
    return min_value,min_value_index
    

def find_max_percent(line):
    x=76
    y=88
    max_value=0
    max_value_index=-1
    for i in range(46):
        try:
            value=float(line[x:y].strip())
        except ValueError:
            continue
        if max_value<value:
            max_value=value
            max_value_index=i
        else:
            pass
        x+=12
        y+=12
    return max_value,max_value_index

def find_gdp(line, index):
    x=76
    y=88
    for i in range(49):
        if i ==index:
            return float(line[x:y].strip())
        else:
            pass
        x+=12
        y+=12
               
def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp):
    min_val_gdp=min_val_gdp/1000
    max_val_gdp=max_val_gdp/1000
    print('\nGross Domestic Product')
    print('{:<10s}{:>8s}{:>6s}{:>18s}'.format('min/max','change','year','GDP (trillions)'))
    print("{:<10s}{:>8f}{:>6d}{:>18.2f}".format("min", min_val, min_year, min_val_gdp))
    print("{:<10s}{:>8f}{:>6d}{:>18.2f}".format("max", max_val, max_year, max_val_gdp))
    
def main():                    
    main_file=open_file()
    line_number=0
    max_percent=max_index=max_gdp=0
    min_percent=min_index=min_gdp=0
    for line in main_file.readlines():
        if line_number==9:
            max_percent=find_max_percent(line)
            min_percent=find_max_percent(line)
        elif line_number==44:
            min_gdp=find_gdp(line,min_index)
            max_gdp=find_gdp(line,max_index)
        else:
            pass
        line_number+=1
    display(min_percent, min_index + 1969, min_gdp, max_percent, max_index + 1969, max_gdp )
        
if __name__ == "__main__":
    main()