

import cards

def less_than(c1,c2):
    '''Return 
           True if c1 is smaller in rank, 
           True if ranks are equal and c1 has a 'smaller' suit
           False otherwise'''
    if c1.rank() < c2.rank():
        return True
    elif c1.rank() == c2.rank() and c1.suit() < c2.suit():
        return True
    return False
    
def min_in_list(L):
    '''Return the index of the mininmum card in L'''
    min_card = L[0]  # first card
    min_index = 0
    for i,c in enumerate(L):
        if less_than(c,min_card):  # found a smaller card, c
            min_card = c
            min_index = i
    return min_index
        
def cannonical(H):
    ''' Selection Sort: find smallest and swap with first in H,
        then find second smallest (smallest of rest) and swap with second in H,
        and so on...'''
    for i,c in enumerate(H):
        # get smallest of rest; +i to account for indexing within slice
        min_index = min_in_list(H[i:]) + i 
        H[i], H[min_index] = H[min_index], c  # swap
    return H

def flush_7(H):
    '''Return a list of 5 cards forming a flush,
       if at least 5 of 7 cards form a flush in H, a list of 7 cards, 
       False otherwise.'''
    pass

def straight_7(H):
    '''Return a list of 5 cards forming a straight,
       if at least 5 of 7 cards form a straight in H, a list of 7 cards, 
       False otherwise.'''
    pass
        
def straight_flush_7(H):
    '''Return a list of 5 cards forming a straight flush,
       if at least 5 of 7 cards form a straight flush in H, a list of 7 cards, 
       False otherwise.'''
    pass

def four_7(H):
    '''Return a list of 4 cards with the same rank,
       if 4 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.'''
    pass

def three_7(H):
    '''Return a list of 3 cards with the same rank,
       if 3 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''
    pass
        
def two_pair_7(H):
    '''Return a list of 4 cards that form 2 pairs,
       if there exist two pairs in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H) and three_7(H) are both False.'''
    pass

def one_pair_7(H):
    '''Return a list of 2 cards that form a pair,
       if there exists exactly one pair in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H), three_7(H) and two_pair(H) are False.'''
    pass

def full_house_7(H):
    '''Return a list of 5 cards forming a full house,
       if 5 of the 7 cards form a full house in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''    
    pass

def main():
    D = cards.Deck()
    D.shuffle()
       
    while True:
        # create community cards
        # create Player 1 hand
        # create Player 2 hand
    
        print("-"*40)
        print("Let's play poker!\n")
        print("Community cards:",community_list)
        print("Player 1:",hand_1_list)
        print("Player 2:",hand_2_list)
        print()
    


if __name__ == "__main__":
    main()
    
    
    
D = cards.Deck()
    the_deck=cards.Deck() 
    while True:
        player1_list=[]
        player2_list=[]
        for i in range (2):
            player1_list.append(the_deck.deal())
            player2_list.append(the_deck.deal())
            community_list=[]
        for i in range (5):
            community_list.append(the_deck.deal())
    
        print("-"*40)
        print("Let's play poker!\n")
        print("Community cards:",community_list)
        print("Player 1:",hand_1_list)
              print("Player 2:",hand_2_list)
        print()
        ipt=input('\nDo you wish to play another hand?(Y or N)')
        if ipt.lower()=='y':
            continue
        
the_deck=cards.Deck()
    while True:
        player1_list=[]
        player2_list=[]
        for i in range (2):
            player1_list.append(the_deck.deal())
            player2_list.append(the_deck.deal())
            community_list=[]

            for i in range (5):
                community_list.append(the_deck.deal())
    print ('-'*40,"\nLet's play poker!\n","\nCommunity cards:",community_list,'\nPlayer1:',player1_list,'\nPlayer2:',player2_list)
    H1=community_list+player1_list
    H2=community_list+player2_list
    rank_list1=['x','Hight card',one_pair_7(H1),two_pair_7(H1),three_7(H1),straight_7(H1),flush_7(H1),full_house_7(H1),four_7(H1),straight_flush_7(H1)]
    rank_list2=['x','High card',one_pair_7(H2),two_pair_7(H2),three_7(H2),straight_7(H2),flush_7(H2),full_house_7(H2),four_7(H2),straight_flush_7(H2)]
    rank_list=['x','High card','one pair','two pairs','three of a kind','straight','flush','full house','four of kind','straight flush']
    for i in range(8,0,-1):
        if rank_list1[i]!=[]:
            rank1=i
            break
  
    for i in range(8,0,-1):
        if rank_list2[i]!=[]:
            rank2=i
            break
  
    if rank1>rank2:
        print('\nPlayer 1 wins with a',rank_list[rank1],':', rank_list1[rank1])
    if rank2>rank1:
        print('\nPlayer 2 wins with a',rank_list[rank2],':', rank_list2[rank2])
  
    if rank1==1 and rank2==1:
        D=build_rank_D(H1)
        height_list=[]  
        for k,v in D.items():
            height_list.append((k,v))
            height_list.sort()
            print('\nTIE with High Card:',height_list[-1][-1])
    if rank1==rank2 and rank1!=1:
        print('\nTIE with a',rank_list[rank2],':',rank_list1[rank1])
    if len(the_deck)<9:
        print('Deck has too few cards so game is done.')
        break
    ipt=input('\nDo you wish to play another hand?(Y or N)')
    if ipt.lower()=='y':
        continue
    else:
        print('The player quit the game.')
        break