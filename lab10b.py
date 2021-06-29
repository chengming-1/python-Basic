import cards
def List(hand):
    p1=[]
    p2=[]
    for i in range(0,5):
        p1.append(hand.deal())
        p2.append(hand.deal())
    return p1,p2
      
def Display(p1, p2):
    print ("Hand1: {}".format(p1))
    print ("Hand2: {}".format(p2))
    
def Display_result(p1, p2):
    print ("hand1: {}".format(p1))
    print ("hand2: {}".format(p2))
 
def Rule(p1_card,p2_card):    
    if p1_card.rank() < p2_card.rank():
        if p1_card.value()!='player2':
            print ("Player 2 wins battle.")
            return 'player2'
        else:
            print ("Player 1 wins battle.")
            return 'player1'
    elif p1_card.rank() > p2_card.rank():
        if p2_card.value()!='player1':
            print ("Player 1 wins battle.")
            return 'player1'
        else:
            print("Player 2 wins battle.")
            return 'player2'
    else:
        print("Tie")
        return 'tie'
    
print("Starting Hands")    
hand= cards.Deck()
p1,p2=List(hand)
Display(p1, p2)
while True:
    p1_card = p1.pop( 0 )
    p2_card = p2.pop( 0 )
    print("Battle was 1: {}, 2: {}.".format(p1_card,p2_card))
    higher=Rule(p1_card,p2_card)
    if higher=='tie':
        p1.append(p1_card)
        p2.append(p2_card)
    elif higher=='player1':
        p1.append(p1_card)
        p1.append(p2_card)
    elif higher=='player2':
        p2.append(p2_card)
        p2.append(p1_card)
    Display_result(p1, p2)
    if len(p1)==0:
        break
    if len(p2)==0:
        break
    c=input("Keep Going: (Nn) to stop:")
    if c.lower()=='n':
        break;
  
if len(p1)> len(p2):
    print ("Player 1 wins!!!")
elif len(p2)>len(p1):
    print ("Player 2 wins!!!")
else:
    print ("Game tie" )




