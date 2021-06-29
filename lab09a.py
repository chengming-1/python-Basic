from operator import itemgetter

def build_map( in_file1, in_file2 ): 
    in_file1.readline()
    in_file2.readline()
    data_map = {}
    for line in in_file1:#READ EACH LINE FROM FILE 
        # Split the line into two words
        countries_list = line.strip().split()
        # Convert to Title case, discard whitespace
        continent = countries_list[0].strip().title()
        country = countries_list[1].strip().title()
        # Ignore empty strings
        if continent != "":
            if continent not in data_map.keys():
                data_map[continent] = {}# If current continent not in map, insert it 
            data_map[continent][country]=[]# If country is not empty insert (continent is guaranteed to be in map)
            if country not in data_map[continent].keys():# If current country not in map, insert it 
                data_map[continent][country] = []
    for line in in_file2:#READ EACH LINE FROM FILE 2        
        # Split the line into two words
        cities_list = line.strip().split()
        # Convert to Title case, discard whitespace
        country = cities_list[0].strip().title()
        city = cities_list[1].strip().title()
        # Ignore empty strings
        if country != "": 
            # insert city (country is guaranteed to be in map)
            for continent in data_map:
                if country in data_map[continent] and city not in data_map[continent][country]:
                    data_map[continent][country].append(city)
    return data_map

def display_map( data_map ):
# Modify this code to display a sorted nested dictionary
    continents_list = sorted(data_map.keys())  #sorted list of the continent keys
    for continents in continents_list:# For each continent
          print("{}:".format(continents)) #continents in continents_list
          countries_list = sorted(data_map[continents]) #sorted list of the countries keys in the continents
          for countries in countries_list:# For each country
                print("{:>10s} --> ".format(countries),end = '') #countries in countries_list
                cities = sorted(data_map[continents][countries])  #sorted list of the cities
                # For each city 
                for city in cities[:-1]:#As long as not last city, add a comma and a space after the cities names
                    print('{}, '.format(city),end = '') # city in cities                      
                      # if it is the last, don't add a comma and a space.
                print('{}'.format(cities[-1])) # city in cities
def open_file():
    try:
        filename = input("Enter file name: ")
        in_file = open( filename, "r" )     
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None
    return in_file

def main():

    in_file1 = open_file() #Continents with countries file: continents.txt
    in_file2 = open_file() #Countries with cities file: cities.txt

    if in_file1 != None and in_file2 != None:

        data_map = build_map( in_file1, in_file2 ) # data_map is a dictionary
        display_map( data_map )
        in_file1.close()
        in_file2.close()

if __name__ == "__main__":
    main()
