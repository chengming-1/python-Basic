import cards
def less_than(c1,c2):
    if c1.rank() < c2.rank():
        return True
    elif c1.rank() == c2.rank() and c1.suit() < c2.suit():
        return True
    return False
   
def min_in_list(L):
    min_card = L[0]
    min_index = 0
    for i,c in enumerate(L):
        if less_than(c,min_card):
            min_card = c
            min_index = i
    return min_index
       
def cannonical(H):
    for i,c in enumerate(H):
        min_index = min_in_list(H[i:]) + i
        H[i], H[min_index] = H[min_index], c 
    return H
def flush_7(H):
    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    list = []
    for i in range(0,len(H)):
        if H[i].suit == 'c':
            list_1.append(H[i])
        elif H[i].suit == 'd':
            list_2.append(H[i])
        elif H[i].suit == 'h':
            list_3.append(H[i])
        elif H[i].suit == 's':
            list_4.append(H[i])
    if len(list_1) == 5:
        return list_1;
    elif len(list_2) == 5:
        return list_2
    elif len(list_3) == 5:
        return list_3;
    elif len(list_4) == 5:
        return list_4;
    return list;
   
def straight_7(H):
    l = cannonical(H)
    a = []
    if len(a) < 1:
        return a
    rn = l[1].value()
    for i in range(0,len(l)):
        if rn == l[i].value():
            a.append()
        else:
            a.clear()
        if rn < 10:
            rn = rn + 1;
    if len(a) == 5:
        return a
    a.clear()
    return a
       
def straight_flush_7(H):
    l = flush_7(H)
    l1 = []
    l2 = []
    if l != None:
        l1 = straight_7(l)
        if l1 != None:
            return l1;
    return l2
def four_7(H):
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
        community_list = []
        for i in range(0,5):
            community_list.append(D.deal())
        hand_1_list = D.deal()
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