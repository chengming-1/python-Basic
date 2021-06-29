
# purchase price and payment will be kept in cents

quarters = 10
dimes = 10
nickels = 10
pennies = 10

print("\nWelcome to change-making program.")

print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))

in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
d_p=input("Input dollars paid(int):")
t_q=0.25*quarters
t_d=0.1*dimes
t_n=0.05*nickels
t_p=0.01*pennies
total=t_q+t_d+t_n+t_p
Quarters=0
Dimes=0
Nickels=0
Pennies=0

while in_str != 'q':
    paid= float(d_p)-float(in_str)
    if float(total)<paid:
        print('Error: ran out of coins')
    elif  float(total)==paid:
        print('No change.')
    elif float(in_str)<0:
        print('Error:insufficient payment')
    elif float(total)>paid:
        Quarters=paid//0.25
        Dimes=(paid%0.25)//0.1
        Nickels=(paid-Quarters*0.25-Dimes*0.1)//0.05
        Pennies=(paid-Quarters*0.25-Dimes*0.1-Nickels*0.05)/0.01
        quarter=10-Quarters
        dimes=10-Dimes
        nickels=10-Nickels
        pennies=10-Pennies
        print("Collect change below:\Quarters:{}\Dimes:{}\Nickels:{}\Pennis:{}".format(Quarters, Dimes, Nickels, Pennies))
        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))
    else:
        break
                

        in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
