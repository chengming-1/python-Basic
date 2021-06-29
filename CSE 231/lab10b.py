import cards
def List(R):
    player1_list=[]
    player2_list=[]
    for i in range( 5 ):
        player1_list.append(R.deal())
        player2_list.append(R.deal())
    return player1_list,player2_list

def Rules(player1_card,player2_card):    
    if player1_card.rank() < player2_card.rank():
        if player1_card.value()!='player2':
            print ("Player 2 wins battle.")
            return 'player2'
        else:
            print ("Player 1 wins battle.")
            return 'player1'
    elif player1_card.rank() > player2_card.rank():
        if player2_card.value()!='player1':
            print ("Player 1 wins battle.")
            return 'player1'
        else:
            print("Player 2 wins battle.")
            return 'player2'
    else:
        print("Tie")
        return 'tie'
       
def Display(player1_list, player2_list):
    print ("Hand1: {}".format(player1_list))
    print ("Hand2: {}".format(player2_list))
    
def Display2(player1_list, player2_list):
    print ("hand1: {}".format(player1_list))
    print ("hand2: {}".format(player2_list))
    
print("Starting Hands")    
R = cards.Deck()
player1_list,player2_list=List(R)
Display(player1_list, player2_list)
while True:
    player1_card = player1_list.pop( 0 )
    player2_card = player2_list.pop( 0 )
    print("Battle was 1: {}, 2: {}.".format(player1_card,player2_card))
    Winner=Rules(player1_card,player2_card)
    if Winner=='tie':
        player1_list.append(player1_card)
        player2_list.append(player2_card)
    elif Winner=='player1':
        player1_list.append(player1_card)
        player1_list.append(player2_card)
    elif Winner=='player2':
        player2_list.append(player2_card)
        player2_list.append(player1_card)
    Display2(player1_list, player2_list)
    if len(player1_list)==0:
        break
    if len(player2_list)==0:
        break
    c=input("Keep Going: (Nn) to stop:")
    if c.lower()=='n':
        break;
  
if len(player1_list)> len(player2_list):
    print ("Player 1 wins!!!")
elif len(player2_list)>len(player1_list):
    print ("Player 2 wins!!!")
else:
    print ("Game tie" )

