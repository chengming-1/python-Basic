VOWELS = "aeiou"
word = input("Enter a word ('quit' to quit): ")
word=word.lower()

while word !='quit':
    if word[0]in VOWELS:
       print(word+'way')
       word = input("Enter a word ('quit' to quit): ")
       word=word.lower()
    else:
        for index,letter in enumerate(word):
            if word[0] not in VOWELS:
                word=word[1:]+word[0]
            else:
                continue

        print(word+'ay')
        word = input("Enter a word ('quit' to quit): ")
        word=word.lower()
      

   
        
# Error message used in Mimir test
#print("Can't convert empty string.  Try again.")
    
    
    
