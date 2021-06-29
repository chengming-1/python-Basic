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
    min_card = L[0] # first card
    min_index = 0
    for i,c in enumerate(L):
        if less_than(c,min_card): # found a smaller card, c
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
        H[i], H[min_index] = H[min_index], c # swap
    return H
def flush_7(H):
    '''Return a list of 5 cards forming a flush,
       if at least 5 of 7 cards form a flush in H, a list of 7 cards,
       False otherwise.'''
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l = []
    for i in range(0,len(H)):
        if H[i].suit == 'c':
            l1.append(H[i])
        elif H[i].suit == 'd':
            l2.append(H[i])
        elif H[i].suit == 'h':
            l3.append(H[i])
        elif H[i].suit == 's':
            l4.append(H[i])
    if len(l1) == 5:
        return l1;
    elif len(l2) == 5:
        return l2
    elif len(l3) == 5:
        return l3;
    elif len(l4) == 5:
        return l4;
    return l;
   
def straight_7(H):
    '''Return a list of 5 cards forming a straight,
       if at least 5 of 7 cards form a straight in H, a list of 7 cards,
       False otherwise.'''
    l = cannonical(H)
    l1 = []
    if len(l) < 1:
        return l1
    rn = l[1].value()
    for i in range(0,len(l)):
        if rn == l[i].value():
            l1.append()
        else:
            l1.clear()
        if rn < 10:
            rn = rn + 1;
    if len(l1) == 5:
        return l1
    l1.clear()
    return l1
       
def straight_flush_7(H):
    '''Return a list of 5 cards forming a straight flush,
       if at least 5 of 7 cards form a straight flush in H, a list of 7 cards,
       False otherwise.'''
    l = flush_7(H)
    l1 = []
    l2 = []
    if l != None:
        l1 = straight_7(l)
        if l1 != None:
            return l1;
    return l2
def four_7(H):
    '''Return a list of 4 cards with the same rank,
       if 4 of the 7 cards have the same rank in H, a list of 7 cards,
       False otherwise.'''
    l1 = cannonical(H)
    l2 = []
    rnk = l1[0].rank()
    for i in range(0,len(l1)):
        if rnk == l1[i].rank():
            l2.append(l1[i])
        else:
            if len(l2) == 4:
                return l2;
            l2.clear()
            rnk = l1[i].rank()
            l2.append(l1[i])
    if len(l2) == 4:
        return l2;
    l2.clear()
    return l2
def three_7(H):
    '''Return a list of 3 cards with the same rank,
       if 3 of the 7 cards have the same rank in H, a list of 7 cards,
       False otherwise.
       You may assume that four_7(H) is False.'''
    l1 = cannonical(H)
    l2 = []
    rnk = l1[0].rank()
    for i in range(0,len(l1)):
        if rnk == l1[i].rank():
            l2.append(l1[i])
        else:
            if len(l2) == 3:
                return l2;
            l2.clear()
            rnk = l1[i].rank()
            l2.append(l1[i])
    if len(l2) == 3:
        return l2;
    l2.clear()
    return l2
       
def two_pair_7(H):
    '''Return a list of 4 cards that form 2 pairs,
       if there exist two pairs in H, a list of 7 cards,
       False otherwise.
       You may assume that four_7(H) and three_7(H) are both False.'''
    l1 = cannonical(H)
    l2 = []
    rnk = l1[0].rank()
    for i in range(0,len(l1)):
        if rnk == l1[i].rank():
            l2.append(l1[i])
        else:
            if len(l2) == 2:
                rnk = l1[i].rank()
                break;
            l2.clear()
            rnk = l1[i].rank()
            l2.append(l1[i])
    for i in range(0,len(l1)):
        if rnk == l1[i].rank():
            l2.append(l1[i])
        else:
            if len(l2) == 4:
                return l2;
            l2.remove(-1)
            rnk = l1[i].rank()
            l2.append(l1[i])
    if len(l2) == 4:
        return l2;
    l2.clear()
    return l2
def one_pair_7(H):
    '''Return a list of 2 cards that form a pair,
       if there exists exactly one pair in H, a list of 7 cards,
       False otherwise.
       You may assume that four_7(H), three_7(H) and two_pair(H) are False.'''
    l1 = cannonical(H)
    l2 = []
    rnk = l1[0].rank()
    for i in range(0,len(l1)):
        if rnk == l1[i].rank():
            l2.append(l1[i])
        else:
            if len(l2) == 2:
                return l2;
            l2.clear()
            rnk = l1[i].rank()
            l2.append(l1[i])
    if len(l2) == 2:
        return l2;
    l2.clear()
    return l2
def full_house_7(H):
    '''Return a list of 5 cards forming a full house,
       if 5 of the 7 cards form a full house in H, a list of 7 cards,
       False otherwise.
       You may assume that four_7(H) is False.'''   
    l1 = three_7(H)
    if l1 == None:
        return l1;
    l2 = cannonical(H)
    rnk = l2[0].rank()
    for i in range(0,len(l2)):
        if rnk == l2[i].rank():
            l1.append(l2[i])
        else:
            if len(l1) == 5:
                return l1;
            l1.remove(-1)
            rnk = l2[i].rank()
            l1.append(l2[i])
    if len(l1) == 5:
        return l1;
    l1.clear()
    return l1
def countScore(l1,l2,l3):
    l = []
    for i in range(0,len(l1)):
        l.append(l1[i])
    l.append(l2)
    l4 = straight_flush_7(l);
    l.pop(-1);
    l.append(l3)
    l5 = straight_flush_7(l)
    if l4 != None and l5 != None:
        print("TIE with Straight Flush ",l4)
        return
    elif l4 == None:
        print("Player 2 Wins with Straight Flush ",l5)
        return;
    elif l5 == None:
        print("Player 1 Wins with Straight Flush ",l4)
        return;
    l5.clear()
    l5 = four_7(l)
    l.remove(-1)
    l.append(l2)
    l4.clear()
    l4 = four_7(l)
    if l4 == None and l5 != None:
        print("Player 2 Wins with Straight Flush ",l5)
        return;
    elif l5 == None and l4 != None:
        print("Player 1 Wins with Straight Flush ",l4)
        return;
    l4.clear()
    l4 = full_house_7(l)
    l.remove(-1)
    l.append(l3)
    l5.clear()
    l5 = full_house_7(l)
    if l4 != None and l5 != None:
        print("TIE with Full House ",l4)
        return
    elif l4 == None:
        print("Player 2 Wins with Full House ",l5)
        return;
    elif l5 == None:
        print("Player 1 Wins with Full House ",l4)
        return;
    l5.clear()
    l5 = three_7(l)
    l.remove(-1)
    l.append(l2)
    l4.clear()
    l4 = three_7(l)
    if l4 != None and l5 != None:
        print("TIE with Three Of A KInd ",l4)
        return
    elif l4 == None:
        print("Player 2 Wins with Three Of A Kind ",l5)
        return;
    elif l5 == None:
        print("Player 1 Wins with Three Of A Kind ",l4)
        return;
    l4.clear()
    l4 = two_pair_7(l)
    l.remove(-1)
    l.append(l3)
    l5.clear()
    l5 = two_pair_7(l)
    if l4 != None and l5 != None:
        print("TIE with Two Pair ",l4)
        return
    elif l4 == None:
        print("Player 2 Wins with Two Pair ",l5)
        return;
    elif l5 == None:
        print("Player 1 Wins with Two Pair ",l4)
        return;
    l5.clear()
    l5 = one_pair_7(l)
    l.remove(-1)
    l.append(l2)
    l4.clear()
    l4 = one_pair_7(l)
    if l4 != None and l5 != None:
        print("TIE with One Pair ",l4)
        return
    elif l4 == None:
        print("Player 2 Wins with One Pair ",l5)
        return;
    elif l5 == None:
        print("Player 1 Wins with One Pair ",l4)
        return;
    l4.clear()
    l4 = flush_7(l)
    l.remove(-1)
    l.append(l3)
    l5.clear()
    l5 = flush_7(l)
    if l4 != None and l5 != None:
        print("TIE with flush ",l4)
        return
    elif l4 == None:
        print("Player 2 Wins with flush ",l5)
        return;
    elif l5 == None:
        print("Player 1 Wins with flush ",l4)
        return;
    l5.clear()
    l5 = straight_7(l)
    l.remove(-1)
    l.append(l2)
    l4.clear()
    l4 = straight_7(l)
    if l4 != None and l5 != None:
        print("TIE with Straight ",l4)
        return
    elif l4 == None:
        print("Player 2 Wins with Straight ",l5)
        return;
    elif l5 == None:
        print("Player 1 Wins with Straight ",l4)
        return;
   
def main():
    D = cards.Deck()     
    while True:
        if len(D) < 9:
            return
        # create community cards
        community_list = []
        for i in range(0,5):
            community_list.append(D.deal())
        # create Player 1 hand
        hand_1_list = D.deal()
        # create Player 2 hand
        hand_2_list = D.deal()
   
        print("-"*40)
        print("Let's play poker!\n")
        print("Community cards:",community_list)
        print("Player 1:",hand_1_list)
        print("Player 2:",hand_2_list)
        countScore(community_list,hand_1_list,hand_2_list)
        y = input("do you wish to play another hand?(Y or N)")
        if y[0] != 'y':
            return
if __name__ == "__main__":
    main()