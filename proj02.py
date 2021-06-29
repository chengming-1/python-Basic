    ###########################################################
    #  Computer Project #2
    #
    #   ensure the numer for total moeny
    #       input the money need paid and the price
    #       compare the total money with need to pay
    #           cauclate the remain money
    #               cauclate the money still need to payback 
    #       output the coin remain
    #    loop until the moeny exhuast or not correct message
    ###########################################################

quarters = 10
dimes = 10
nickels = 10
pennies = 10 #numbers of coins
print("Welcome to change-making program.")
print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))
in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
use_qua=0
use_dim=0
use_nic=0
use_pen=0 #numbers of used coins
while in_str != 'q':
    if float(in_str)<0:
        print('Error: purchase price must be non-negative.')
        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(int(quarters), int(dimes), int(nickels), int(pennies)))
        in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
    money_give = input("Input dollars paid (int): ")
    paid= float(money_give)-float(in_str)
    total=quarters*0.25+dimes*0.1+nickels*0.05+pennies*0.01
    if  float(in_str)==float(money_give):
        print('No change.')  # for no change
        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(int(quarters), int(dimes), int(nickels), int(pennies)))
        in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
        continue# renturn the loop
    elif float(in_str)>float(money_give):
        print('Error: insufficient payment.')
        continue #return the loop if money is not enough

    elif float(total)>float(paid) :
        paid = float(money_give)-float(in_str) #money need payback to customer
        while quarters>0 and (paid % quarters) >=0.25: # if quarters still more than 0 and the paid still higher than 0.25
            quarters-=1
            use_qua +=1
            paid-=0.25
        while dimes>0 and (paid% dimes) >= 0.1:# if dimes still more than 0 and the paid still higher than 0.1
            dimes-=1
            use_dim+=1
            paid-=0.1
        while nickels>0 and (paid% nickels) >= 0.05:# if nickels still more than 0 and the paid still higher than 0.05
            nickels-=1
            use_nic+=1
            paid-=0.05
        while pennies>0 and (paid% pennies)>= 0.0099:# if pennies still more than 0 and the paid still higher than 0.01
            pennies-=1
            use_pen+=1
            paid-=0.0099
        print()
    elif quarters == dimes == nickels == pennies == 0 or paid>total: #no enough money to payback
        print('Error: ran out of coins.')
        break
    print ("Collect change below: ")
    if use_qua > 0:
        print("Quarters:",use_qua)
    if use_dim > 0:
        print("Dimes:",use_dim)
    if use_nic > 0:
        print( "Nickels:",use_nic)
    if use_pen > 0:
        print("Pennies:", use_pen) #count the number used
    use_qua=0
    use_dim=0
    use_nic=0
    use_pen=0 #return to zero for next loop
    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(int(quarters), int(dimes), int(nickels), int(pennies)))
    in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

                

