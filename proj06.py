    ###########################################################
    #  Computer Project #6
    #   import cards
    #   def less than for card1 and card2
    #   def to find mins card in list
    #   def for list the card
    #   def flush
    #   def straight
    #   def straight_flush
    #   def one pair
    #   def two pairs
    #   def display for cards in different catagory
    #   def main function for shuffle cards and display
    ###########################################################
import cards
def less_than(c1,c2):# compared 
    if c1.rank() < c2.rank():
        return True
    elif c1.rank() == c2.rank() and c1.suit() < c2.suit():
        return True
    return False
   
def min_in_list(List):#find the mins in the list
    min_card = List[0]
    min_index = 0
    for i,ch in enumerate(List):
        if less_than(ch,min_card):
            min_card = ch
            min_index = i
    return min_index
       
def cannonical(h):
    for i,ch in enumerate(h):
        min_index = min_in_list(h[i:]) + i
        h[i], h[min_index] = h[min_index], ch
    return h

def flush_7(h):#same kinds of color
    color = []    #cata
    for i,ch in enumerate(h):
        color.append(ch.suit())
    rs = []#result
    for a in color:
        if color.count(a) >= 5:
            for ch in h:
                if ch.suit() == a:
                    rs.append(ch)
                if len(rs) == 5: 
                    break
        if len(rs) == 5:
            break
    if rs:
         return rs
    else:
        return False
def straight_7(h):#sequence of 5 cards
    t=[]#instead of straight
    straight=[]
    cannonical(h)
    for i in range(0,len(h)-1):
        if h[i].rank()+1==h[i+1].rank():
            if h[i] not in straight:
                straight.append(h[i])
            if h[i+1] not in straight:
                straight.append(h[i+1])
    if len(straight)<5:
        return False
    if len(straight)==5:
        t=straight
        for i in range(0,4):
            a=t[i].rank()
            b=t[i+1].rank()
            if a+1==b:
                ''
            else:
                return False
    if len(straight)==6:
        t=straight[0:5]
        for i in range(0,4):
            a=t[i].rank()
            b=t[i+1].rank()
            if a+1==b:
                ''
            else:
                return False
    if len(straight)==7:
        t=straight[0:5]
        for i in range(0,4):
            a=t[i].rank()
            b=t[i+1].rank()
            if a+1==b:
                ''
            else:
                t=straight[2:7]
                for i in range(0,4):
                    a=t[i].rank()
                    b=t[i+1].rank()
                    if a+1==b:
                        ''
                    else:
                        return False
    if not False:
        return t
                
        
                
def straight_flush_7(h):#same colors and sequence
    L=[]
    if straight_7(h) is not False:
        L=straight_7(h)
        if flush_7(L) is not False:
            return L
        else:
            return False
    else:
        return False
    
def four_7(h):#four of 5 are same
    n = []
    for i,ch in enumerate(h):
        n.append(ch.rank())
    return_list = []
    for a in n:
        if n.count(a) == 4:
            for ch in h: 
                if ch.rank() == a:
                    return_list.append(ch)
                if len(return_list) == 4:
                    break
        if len(return_list) == 4:
            break
    if return_list:
        return return_list
    else:
        return False
def three_7(h):#3 of 5 are same
    color=[] 
    rs=[]#result
    for i,ch in enumerate(h): 
        color.append(ch.rank())   
    for a in color: 
        if color.count(a) == 3: 
            for ch in h: 
                if ch.rank() == a: 
                    rs.append(ch)
                if len(rs) == 3: 
                    break
        if len(rs) == 3: 
            break
    if rs:
        return rs
    else:
        return False
    
def two_pair_7(h):# two group cards
    val = {}
    rs=[]
    for i in h:
        if i.rank() not in val:
            val[i.rank()] = 1 
        else:
            val[i.rank()] += 1
    num_list=[]
    for d,v in val.items(): 
        if v == 2: 
             num_list.append(d)
             num_list.append(d)  
    if len(num_list)==4:
        i=0
        for n in num_list:
            for ch in h:
                if ch.rank() == n and ch not in rs: 
                    rs.append(ch) 
        return rs
    else:
        return False
def one_pair_7(h):#have 1 pair card
    val = {} 
    rs = []
    num_list=[]
    for i in h: 
        if i.rank() not in val : 
            val [i.rank()] = 1
        else:
            val [i.rank()] += 1            
    for d,v in val .items(): 
        if v == 2: 
            num_list.append(d) 
            num_list.append(d) 
    if len(num_list) == 2:
        i=0
        for ch in h:
            if ch.rank() == num_list[i]: 
                i+=1
                rs.append(ch)
            if i==2:
                break
        return rs
    else:
        return False
def get(p1, p2, kind):
    if kind == 'straight flush':
        return (straight_flush_7(p1), straight_flush_7(p2))
    if kind == '4 of a kind':
        return (four_7(p1), four_7(p2))
    if kind == 'full house':
        return (full_house_7(p1), full_house_7(p2))
    if kind == 'flush':
        return (flush_7(p1), flush_7(p2))
    if kind == 'straight':
        return (straight_7(p1), straight_7(p2))
    if kind == '3 of a kind':
        return (three_7(p1), three_7(p2))
    if kind == '2 pair':
        return (two_pair_7(p1), two_pair_7(p2))
    if kind == '1 pair':
        return (one_pair_7(p1), one_pair_7(p2))
    return (p1, p2)
    
def full_house_7(h):# 3 same with 2 same
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
        return cannonical(rs) 
    else:
        return False

def main():
    D = cards.Deck()  
    D.shuffle()     
    while True:
        full = False
        List = []
        for i in range(9):        #limited range
            card = D.deal()
            if card:
                List.append(card)
            else:
                full = True 
                break
        p1_list = List[5:7]
        p2_list = List[7:9]
        community_list = List[0:5]
        H1 = cannonical(p1_list + community_list)
        H2 = cannonical(p2_list + community_list)
        print("-"*40)
        print("Let's play poker!\n")
        print("Community cards:",community_list)
        print("Player 1:",p1_list)
        print("Player 2:",p2_list)        
        if flush_7(H1):   
            if flush_7(H2):
                print("\nTIE with a flush:", flush_7(H1))
            else:
                print("\nPlayer 1 wins a with flush:", flush_7(H1))
        elif flush_7(H2):
            print("\nPlayer 2 wins a with flush:", flush_7(H2))
        elif straight_7(H1):  
            if straight_7(H2):
                print("\nTIE with straight:", straight_7(H1))
            else:
                print("\nPlayer 1 wins with straight:", straight_7(H1))
        elif straight_7(H2):
            print("\nPlayer 2 wins with straight:", straight_7(H2))
        elif straight_flush_7(H1):    
            if straight_flush_7(H2):
                print("\nTIE with straight flush:", straight_flush_7(H1))
            else:
                print("\nPlayer 1 wins with straight flush:", straight_flush_7(H1))
        elif straight_flush_7(H2):
            print("\nPlayer 2 wins with straight flush:", straight_flush_7(H2))
        elif four_7(H1):
            if four_7(H2):
                print("\nTIE with four of a kind:", four_7(H1))
            else:
                print("\nPlayer 1 wins with four of a kind:", four_7(H1))
        elif four_7(H2):
            print("\nPlayer 2 wins with four of a kind:", four_7(H2))
        elif full_house_7(H1):  
            if full_house_7(H2):
                print("\nTIE with a full house:", full_house_7(H1))
            else:
                print("\nPlayer 1 wins with a full house:", full_house_7(H1))
        elif full_house_7(H2):
            print("\nPlayer 2 wins with a full house:", full_house_7(H2))
        elif flush_7(H1):  
            if flush_7(H2):
                print("\nTIE with flush:", flush_7(H1))
            else:
                print("\nPlayer 1 wins with flush:", flush_7(H1))
        elif flush_7(H2):
            print("\nPlayer 2 wins with flush:", flush_7(H2))
        elif three_7(H1):   
            if three_7(H2):
                print("\nTIE with three of a kind:", three_7(H1))
            else:
                print("\nPlayer 1 wins with three of a kind:", three_7(H1))
        elif three_7(H2):
            print("\nPlayer 2 wins with three of a kind:", three_7(H2))
        elif two_pair_7(H1):  
            if two_pair_7(H2):
                print("\nTIE with two pairs:", two_pair_7(H1))
            else:
                print("\nPlayer 1 wins with two pairs:", two_pair_7(H1))
        elif two_pair_7(H2):
            print("\nPlayer 2 wins with two pairs:", two_pair_7(H2))
        elif one_pair_7(H1): 
            if one_pair_7(H2):
                print("\nTIE with one pair:", one_pair_7(H1))
            else:
                print("\nPlayer 1 wins with one pair:", one_pair_7(H1))
        elif one_pair_7(H2):
            print("\nPlayer 2 wins with one pair:", one_pair_7(H2))
        else:  
            print("\nTIE with normal cards")
        if full:
            print("Deck has too few cards so game is done.")
            break
        if len(D)<9:
            print("Deck has too few cards so game is done.")
            break
        ipt = input("\nDo you wish to play another hand?(Y or N) ")
        if ipt.lower() !='y':
            break
if __name__ == "__main__":
    main()