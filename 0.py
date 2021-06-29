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
    H.sort(key=lambda card: card.suit())
    for i in range(len(H) - 5 + 1):
        if H[i].suit() == H[(i + 4)].suit():
            return H[i:i+5]
    return []
    pass
def straight_7(H):
    '''Return a list of 5 cards forming a straight,
       if at least 5 of 7 cards form a straight in H, a list of 7 cards,
       False otherwise.'''
    H.sort(key=lambda card: card.rank())
    for i in range(len(H) - 5 + 1):
        end = i + 1
        while end < len(H):
            if H[end].rank() - H[end - 1].rank() != 1:
                break
            end = end + 1
        if end - i >= 5:
            return H[i:i + 5]
    return []
    pass
    
        
def straight_flush_7(H):
    '''Return a list of 5 cards forming a straight flush,
       if at least 5 of 7 cards form a straight flush in H, a list of 7 cards,
       False otherwise.'''
    H.sort(key=lambda card: card.rank())
    for i in range(len(H) - 5 + 1):
        end = i + 1
        while end < len(H):
            if H[end].suit() != H[end - 1].suit():
                break
            if H[end].rank() - H[end - 1].rank() != 1:
               break
            end = end + 1
        if end - i >= 5: # found
            return H[i:i + 5]
    return []
    pass
def three_7(H):
    '''Return a list of 3 cards with the same rank,
       if 3 of the 7 cards have the same rank in H, a list of 7 cards,
       False otherwise.
       You may assume that four_7(H) is False.'''
    
    H.sort(key=lambda card: (card.rank()))
    for i in range(len(H) - 3 + 1):
        if H[i].rank() == H[i + 2].rank():
            return H[i:i+3]
    return []
    #pass
def four_7(H):
    '''Return a list of 4 cards with the same rank,
       if 4 of the 7 cards have the same rank in H, a list of 7 cards,
       False otherwise.'''
    H.sort(key=lambda card: card.rank())
    for i in range(len(H) - 4 + 1):
        if H[i].rank() == H[i + 3].rank():
            return H[i:i+4]
    return []
    pass
def one_pair_7(H):
    '''Return a list of 2 cards that form a pair,
       if there exists exactly one pair in H, a list of 7 cards,
       False otherwise.  
       You may assume that four_7(H), three_7(H) and two_pair(H) are False.'''
    H.sort(key=lambda card: card.get_rank())
    # Loop
    for lStrt in range(len(cards) - 2 + 1):
        if H[lStrt].rank() == H[lStrt + 1].get_rank():
            return H[lStrt:lStrt+2]
    return []
    pass
        
def two_pair_7(H):
    '''Return a list of 4 cards that form 2 pairs,
       if there exist two pairs in H, a list of 7 cards,
       False otherwise.  
       You may assume that four_7(H) and three_7(H) are both False.'''
    op = one_pair_7(H)
    if op:
        remaining = [c for c in H if c not in op]
        ap = one_pair_7(remaining)
        if ap:
            op.extend(ap)
            return op
    return []
    pass
 
def full_house_7(h):
    '''Return a list of 5 cards forming a full house,
       if 5 of the 7 cards form a full house in H, a list of 7 cards,
       False otherwise.
       You may assume that four_7(H) is False.'''
    h = h.copy()
    color = [] 
    rs = []
    for i,ch in enumerate(h):
        color.append(ch.rank()) 
    
    for a in color:
        if color.count(a) == 3: 
            for ch in h: 
                if ch.rank() == a: 
                    rs.append(ch)
                    h.remove(ch)
                if len(rs) == 3: 
                    break
        if len(rs) == 3:         
            break 
    if len(rs) == 3: 
        list2=[]
        for b in h:
            list2.append(b.rank()) 
        for l in list2: 
            if list2.count(l) == 2: 
                for ch in h:
                    if ch.rank() == l: 
                        rs.append(ch) 
                    if len(rs) == 5: 
                        break
            if len(rs) == 5:
                break
    if len(rs) == 5: 
        return rs
    else:
        return False
    
def get(player1, player2, cat):
    if cat == 'straight flush':
        return (straight_flush_7(player1), straight_flush_7(player2))
    if cat == '4 of a kind':
        return (four_7(player1), four_7(player2))
    if cat== 'full house':
        return (full_house_7(player1), full_house_7(player2))
    if cat == 'flush':
        return (flush_7(player1), flush_7(player2))
    if cat == 'straight':
        return (straight_7(player1), straight_7(player2))
    if cat == '3 of a kind':
        return (three_7(player1), three_7(player2))
    if cat == '2 pair':
        return (two_pair_7(player1), two_pair_7(player2))
    if cat == '1 pair':
        return (one_pair_7(player1), one_pair_7(player2))
    return (player1, player2)
def main():
    D = cards.Deck()
    D.shuffle()
    community_list = []
    hand_1_list = []
    hand_2_list = []
    hand_1_list.append(D.deal())
    hand_2_list.append(D.deal())
    hand_1_list.append(D.deal())
    hand_2_list.append(D.deal())
    for li in range(5):
        community_list.append(D.deal())
    print ()
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
        hand_1_list.extend(community_list)
        hand_2_list.extend(community_list)
        for cat in ('straight flush', '4 of a kind', 'full house',
                     'flush', 'straight', '3 of a kind', '2 pair', '1 pair', 'high card'):
            play1, play2 = get(hand_1_list, hand_2_list, cat)
            if play1 and play2:
                print ("TIE with a %s: %s" % (cat, play1))
                break
            elif play1 and not play2:
                print ("Player %d wins with a %s: %s" % (1, cat, play1))
                break
            elif not play1 and play2:
                print ("Player %d wins with a %s: %s" % (2, cat, play2))
                break
        if D.cards_count() < 9:
            print ("Deck has too few cards so game is done.")
            break
        print ()
        c = input ("Do you wish to play another hand? (Y or N) ")
        if c not in ('y', 'Y'):
            break
    
if __name__ == "__main__":
    main()