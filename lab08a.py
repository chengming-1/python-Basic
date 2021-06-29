
import string
from operator import itemgetter


def add_word( word_map, word ):
    if word:
        word=word.lower()
    # to make the letter become lower for any format
        if word not in word_map:
           word_map[ word ] = 0
    # add to dictionary
        word_map[ word ] += 1


def build_map( in_file, word_map ):

    for line in in_file:

        # split the line as list
        word_list = line.split()
        for word in word_list:
            # remove the punctutation and space, and then add to dictionary
            word = word.strip().strip(string.punctuation)
            word= word.lower()
            add_word( word_map, word )
        

def display_map( word_map ):
    word_list = list()
    # add count and words from  dictionary and then append to tuples
    for word, count in word_map.items():
        word_list.append( (word, count) )
    # sort the list and consequence
    freq_list = sorted( word_list)
    freq_list = sorted(sorted(word_list, key=lambda word_tuple: word_tuple[0]), key=lambda word_tuple: word_tuple[1],reverse=True)
    print("Enter file name:")
    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )


def open_file():

    try:
        in_file = open( "document1.txt", "r" )     
    except IOError:
        in_file = open( "document2.txt", "r" )
    return in_file


word_map = dict()
in_file = open_file()

if in_file != None:

    build_map( in_file, word_map )
    display_map( word_map )
    in_file.close()


