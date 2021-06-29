# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 21:00:55 2018

@author: 73251
"""
def straight_7(H):#sequence five value
H=cannonical(H)
    rst=[]
    rst2=[]
    n=[]
    for i,c in enumerate(H):
        n.append(c.rank())
    n.sort()
    min_rank = min(n)
    while True:
        if min_rank in n and (min_rank + 1) in n and (min_rank + 2) in n and (min_rank + 3) in n and (min_rank + 4) in n:
            for h in H:
                if h.rank() == min_rank and h.rank() not in rst2:
                    rst.append(h)
                    rst2.append(h.rank())
                if h.rank() == min_rank + 1 and h.rank() not in rst2:
                    rst.append(h)
                    rst2.append(h.rank())
                if h.rank() == min_rank + 2 and h.rank() not in rst2:
                    rst.append(h)
                    rst2.append(h.rank())
                if h.rank() == min_rank + 3 and h.rank() not in rst2:
                    rst.append(h)
                    rst2.append(h.rank())
                if h.rank() == min_rank + 4 and h.rank() not in rst2:
                    rst.append(h)
                    rst2.append(h.rank())
        if min_rank + 4 == max(n) or len(rst) == 5:
            break
        else:
            min_rank+=1
        if rst:
            return rst
        else:
            return False
        
        
D = cards.Deck() 
    D.shuffle()
    rank_list = ["High card", "one pair", "two pairs", "three of a kind", "straight", "flush", "full house", "four of a kind", "straight flush"]
    while True: 
        if len(D) < 9:
            print("Deck has too few cards so game is done.") 
            break
        community_list = [] 
        for i in range(0,5):
            community_list.append(D.deal())
        hand_1_list = D.deal()
        hand_2_list = D.deal()
        for i in range(2):
            hand_1_list.append(D.deal()) 
        for i in range(2):
            hand_2_list.append(D.deal()) 
        game_hand1 = hand_1_list + community_list 
        game_hand2 = hand_2_list + community_list
        rank_level_hand1 = 10        
        rank_level_hand2 = 10        
        if straight_flush_7(game_hand1) :            
            return_list1 = straight_flush_7(game_hand1)            
            rank_level_hand1 = 9        
        elif four_7(game_hand1):            
            return_list1 = four_7(game_hand1)            
            rank_level_hand1 = 8        
        elif full_house_7(game_hand1):            
            return_list1 = full_house_7(game_hand1)            
            rank_level_hand1 = 7        
        elif flush_7(game_hand1):            
            return_list1 = flush_7(game_hand1)           
            rank_level_hand1 = 6        
        elif straight_7(game_hand1):            
            return_list1 = straight_7(game_hand1)            
            rank_level_hand1 = 5        
        elif three_7(game_hand1):            
            return_list1 = three_7(game_hand1)            
            rank_level_hand1 = 4        
        elif two_pair_7(game_hand1):            
            return_list1 = two_pair_7(game_hand1)            
            rank_level_hand1 = 3        
        elif one_pair_7(game_hand1):            
            return_list1 = one_pair_7(game_hand1)            
            rank_level_hand1 = 2        
        else:            
            rank_level_hand1 = 1            
        if straight_flush_7(game_hand2) :            
            return_list2 = straight_flush_7(game_hand2)            
            rank_level_hand2 = 9        
        elif four_7(game_hand2):            
            return_list2 = four_7(game_hand2)            
            rank_level_hand2 = 8        
        elif full_house_7(game_hand2):            
            return_list2 = full_house_7(game_hand2)            
            rank_level_hand2 = 7        
        elif flush_7(game_hand2):            
            return_list2 = flush_7(game_hand2)            
            rank_level_hand2 = 6        
        elif straight_7(game_hand2):            
            return_list2 = straight_7(game_hand2)           
            rank_level_hand2 = 5        
        elif three_7(game_hand2):            
            return_list2 = three_7(game_hand2)            
            rank_level_hand2 = 4        
        elif two_pair_7(game_hand2):            
            return_list2 = two_pair_7(game_hand2)            
            rank_level_hand2 = 3        
        elif one_pair_7(game_hand2):            
            return_list2 = one_pair_7(game_hand2)            
            rank_level_hand2 = 2       
        else:            
            rank_level_hand2 = 1 
        print("-"*40)
        print("Let's play poker!\n")
        print("Community cards:",community_list)
        print("Player 1:",hand_1_list)
        print("Player 2:",hand_2_list)
        if rank_level_hand1 == rank_level_hand2 == 1:
            print('TIE with high card')        
        elif rank_level_hand1 == rank_level_hand2:            
            print('TIE with '+str(rank_list[rank_level_hand1-1])+':',cannonical(return_list1))        
        elif rank_level_hand1 > rank_level_hand2:            
            print('Player 1 wins with '+str(rank_list[rank_level_hand1-1])+':',cannonical(return_list1))        
        elif rank_level_hand1 < rank_level_hand2:            
            print('Player 2 wins with '+str(rank_list[rank_level_hand2-1])+':',cannonical(return_list2))
        if len(D) < 9:            
            print("Deck has too few cards so game is done.")            
            break                
        input_str = input('Do you wish to play another hand?(Y or N) ')        
        if input_str.lower() == 'y':            
            pass        
        else:            
            break